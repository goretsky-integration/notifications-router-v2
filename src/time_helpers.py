from datetime import datetime, timedelta
from typing import Final, TypeAlias

import humanize

__all__ = (
    'MINUTE_IN_SECONDS',
    'HOUR_IN_SECONDS',
    'DAY_IN_SECONDS',
    'abbreviate_time_units',
    'compute_duration',
    'humanize_stop_sale_duration',
    'is_urgent',
    'humanize_seconds',
)

MINUTE_IN_SECONDS: Final[int] = 60
HOUR_IN_SECONDS: Final[int] = MINUTE_IN_SECONDS * 60
DAY_IN_SECONDS: Final[int] = HOUR_IN_SECONDS * 24

TimeUnitsAndAbbreviation: TypeAlias = tuple[tuple[str, ...], str]


def abbreviate_time_units(text: str) -> str:
    time_units_and_abbreviations: tuple[TimeUnitsAndAbbreviation, ...] = (
        (('дней', 'день', 'дня'), 'дн'),
        (('часов', 'часа', 'час',), 'ч'),
        (('минута', 'минуты', 'минут'), 'мин'),
    )
    words = set(text.split())
    for time_units, abbreviation in time_units_and_abbreviations:
        for time_unit in time_units:
            if time_unit not in words:
                continue
            text = text.replace(time_unit, abbreviation)
    return text


def compute_duration(started_at: datetime) -> timedelta:
    return datetime.utcnow() + timedelta(hours=3) - started_at


def humanize_stop_sale_duration(duration: timedelta) -> str:
    stop_duration_in_seconds = duration.total_seconds()

    if stop_duration_in_seconds >= DAY_IN_SECONDS:
        kwargs = {
            'format': '%0.0f',
            'minimum_unit': 'days',
            'suppress': ['months'],
        }
    elif stop_duration_in_seconds >= HOUR_IN_SECONDS:
        kwargs = {'format': '%0.0f', 'minimum_unit': 'hours'}
    elif stop_duration_in_seconds >= MINUTE_IN_SECONDS:
        kwargs = {'format': '%0.0f', 'minimum_unit': 'minutes'}
    else:
        kwargs = {'format': '%0.0f', 'minimum_unit': 'seconds'}

    return abbreviate_time_units(humanize.precisedelta(duration, **kwargs))


def is_urgent(duration: timedelta) -> bool:
    return duration.total_seconds() >= MINUTE_IN_SECONDS * 30


def humanize_seconds(seconds: int) -> str:
    """Humanize time in seconds.

    Examples:
        >>> humanize_seconds(60)
        '01:00'
        >>> humanize_seconds(0)
        '00:00'
        >>> humanize_seconds(3600)
        '01:00:00'
        >>> humanize_seconds(9000000)
        '+99:59:59'

    Args:
        seconds: Time in seconds.

    Returns:
        Humanized time in HH:MM:SS or MM:SS format.
        If there are over 100 hours (359999 seconds), returns "+99:59:59".
    """
    if seconds > 359999:
        return '+99:59:59'
    minutes = seconds // 60
    seconds %= 60
    hours = minutes // 60
    minutes %= 60
    if not hours:
        return f'{minutes:02}:{seconds:02}'
    return f'{hours:02}:{minutes:02}:{seconds:02}'

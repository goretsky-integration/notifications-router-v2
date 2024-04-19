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

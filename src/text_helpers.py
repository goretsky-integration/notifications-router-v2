from typing import Final

__all__ = ('abbreviate_unit_name', 'ERROR_CODE_TO_MESSAGE', 'int_gaps')


def int_gaps(number: int) -> str:
    """Add gaps to integer number.

    Examples:
        >>> int_gaps(123456789)
        '123 456 789'
        >>> int_gaps(123)
        '123'

    Args:
        number: Integer number.

    Returns:
        Integer number with gaps.
    """
    return '{:,}'.format(number).replace(',', ' ')


def abbreviate_unit_name(unit_name: str) -> str:
    """Contract department name via abbreviations.

    Examples:
        >>> abbreviate_unit_name('Москва 4-1')
        '4-1'
        >>> abbreviate_unit_name('Вязьма-2')
        'ВЗМ-2'
        >>> abbreviate_unit_name('Калуга-4')
        'КЛ-4'

    Args:
        unit_name: Unit name.

    Returns:
        Contracted department name or department name itself without changes
        if department name is not in special replacing map.
    """
    replacing_map = (
        ('вязьма', 'ВЗМ'),
        ('калуга', 'КЛ'),
        ('смоленск', 'СМ'),
        ('обнинск', 'ОБН'),
        ('москва', ''),
        ('подольск', 'П'),
    )
    unit_name = unit_name
    for replaceable, replace_to in replacing_map:
        if replaceable in unit_name.lower():
            return unit_name.lower().replace(replaceable, replace_to).lstrip()
    return unit_name


ERROR_CODE_TO_MESSAGE: Final[dict[str, str]] = {
    'MISSING_DATA': 'отсутствуют данные',
}

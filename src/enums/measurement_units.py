from enum import StrEnum

__all__ = ('MeasurementUnit',)


class MeasurementUnit(StrEnum):
    QUANTITY = 'Quantity'
    KILOGRAM = 'Kilogram'
    LITER = 'Liter'
    METER = 'Meter'

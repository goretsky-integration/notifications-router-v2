from enum import StrEnum, auto

__all__ = ('SalesChannel',)


class SalesChannel(StrEnum):
    DINE_IN = auto()
    TAKEAWAY = auto()
    DELIVERY = auto()

from enum import StrEnum

__all__ = ('EventType',)


class EventType(StrEnum):
    LATE_DELIVERY_VOUCHERS = 'LATE_DELIVERY_VOUCHERS'
    WRITE_OFFS = 'WRITE_OFFS'
    STOPS_AND_RESUMES = 'STOPS_AND_RESUMES'

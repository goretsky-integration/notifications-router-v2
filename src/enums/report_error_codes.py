from enum import StrEnum, auto

__all__ = ('ReportErrorCode',)


class ReportErrorCode(StrEnum):
    AUTH_ERROR = auto()
    API_ERROR = auto()
    REPORTS_SERVICE_ERROR = auto()

from pydantic import BaseModel

from enums import ReportErrorCode

__all__ = ('UnitHeatedShelfStatistics',)


class UnitHeatedShelfStatistics(BaseModel):
    unit_name: str
    average_heated_shelf_time_in_seconds: int | None
    trips_with_one_orders_percentage: int | None
    average_heated_shelf_time_error: ReportErrorCode | None
    trips_with_one_orders_error: ReportErrorCode | None

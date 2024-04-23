from pydantic import BaseModel

__all__ = ('UnitDeliverySpeedStatistics',)


class UnitDeliverySpeedStatistics(BaseModel):
    unit_name: str
    average_cooking_time_in_seconds: int | None = None
    average_delivery_order_fulfillment_time_in_seconds: int | None = None
    average_heated_shelf_time_in_seconds: int | None = None
    average_order_trip_time_in_seconds: int | None = None
    error_code: str | None = None

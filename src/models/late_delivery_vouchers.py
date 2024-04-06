from pydantic import BaseModel

__all__ = ('UnitLateDeliveryVouchers',)


class UnitLateDeliveryVouchers(BaseModel):
    unit_name: str
    certificates_count_today: int
    certificates_count_week_before: int

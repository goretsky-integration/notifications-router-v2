from pydantic import BaseModel, conlist

__all__ = (
    'UnitRevenueStatistics',
    'TotalRevenueStatistics',
    'RevenueStatistics',
)


class UnitRevenueStatistics(BaseModel):
    unit_name: str
    revenue_today: int
    growth_from_week_before_in_percents: int


class TotalRevenueStatistics(BaseModel):
    revenue_today: int
    growth_from_week_before_in_percents: int


class RevenueStatistics(BaseModel):
    units: conlist(UnitRevenueStatistics, min_length=1)
    total: TotalRevenueStatistics

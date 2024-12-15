from typing import Annotated

from pydantic import BaseModel, Field

__all__ = (
    "UnitSalesStatistics",
    "TotalSalesStatistics",
    "SalesStatistics",
)


class UnitSalesStatistics(BaseModel):
    unit_name: str
    sales_for_today: int
    sales_growth_from_week_before_in_percents: int


class TotalSalesStatistics(BaseModel):
    sales_for_today: int
    sales_growth_from_week_before_in_percents: int


class SalesStatistics(BaseModel):
    units: Annotated[list[UnitSalesStatistics], Field(min_length=1)]
    total: TotalSalesStatistics

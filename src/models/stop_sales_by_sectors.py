from datetime import datetime

from pydantic import BaseModel

__all__ = ('StopSaleBySector', 'UnitStopSalesBySectors')


class StopSaleBySector(BaseModel):
    started_at: datetime
    sector_name: str


class UnitStopSalesBySectors(BaseModel):
    unit_name: str
    stop_sales: tuple[StopSaleBySector, ...]

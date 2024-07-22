from datetime import datetime

from pydantic import BaseModel

from enums import StopSaleSalesChannel

__all__ = ('StopSaleBySalesChannel',)


class StopSaleBySalesChannel(BaseModel):
    unit_name: str
    started_at: datetime
    reason: str
    sales_channel: StopSaleSalesChannel

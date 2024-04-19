from datetime import datetime

from pydantic import BaseModel

from enums import SalesChannel

__all__ = ('StopSaleBySalesChannel',)


class StopSaleBySalesChannel(BaseModel):
    unit_name: str
    started_at: datetime
    reason: str
    sales_channel: SalesChannel

from datetime import datetime

from pydantic import BaseModel

__all__ = ('CheatedOrder', 'UnitCheatedOrders')


class CheatedOrder(BaseModel):
    created_at: datetime
    number: str


class UnitCheatedOrders(BaseModel):
    unit_name: str
    phone_number: str
    orders: list[CheatedOrder]

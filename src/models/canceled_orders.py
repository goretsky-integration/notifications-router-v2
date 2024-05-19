from uuid import UUID

from pydantic import BaseModel, conlist

from enums import CountryCode, SalesChannel

__all__ = ('CanceledOrder', 'UnitCanceledOrders')


class CanceledOrder(BaseModel):
    id: UUID
    number: str
    price: int
    sales_channel: SalesChannel
    is_refund_receipt_printed: bool


class UnitCanceledOrders(BaseModel):
    unit_name: str
    orders: conlist(item_type=CanceledOrder, min_length=1)
    country_code: CountryCode

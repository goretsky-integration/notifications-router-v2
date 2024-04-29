from uuid import UUID

from pydantic import BaseModel, conlist

from enums import CountryCode, SalesChannel

__all__ = ('CanceledOrder', 'UnitCanceledOrders')


class CanceledOrder(BaseModel):
    id: UUID
    number: str
    price: int
    sales_channel: SalesChannel
    has_printed_receipt: bool


class UnitCanceledOrders(BaseModel):
    unit_name: str
    orders: conlist(item_type=CanceledOrder, min_length=1)
    country_code: CountryCode

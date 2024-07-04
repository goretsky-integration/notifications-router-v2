from pydantic import BaseModel, conlist

__all__ = (
    'OrderWithoutPrintedReceipt',
    'UnitUnprintedReceipts',
)


class OrderWithoutPrintedReceipt(BaseModel):
    number: str
    price: int


class UnitUnprintedReceipts(BaseModel):
    unit_name: str
    orders: conlist(OrderWithoutPrintedReceipt, min_length=1)

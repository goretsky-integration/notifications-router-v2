from pydantic import BaseModel

__all__ = ('InventoryStockItem', 'UnitInventoryStockItems')


class InventoryStockItem(BaseModel):
    name: str
    quantity: float
    measurement_unit: str


class UnitInventoryStockItems(BaseModel):
    unit_name: str
    inventory_stock_items: list[InventoryStockItem]

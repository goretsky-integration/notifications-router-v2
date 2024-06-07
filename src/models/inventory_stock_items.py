from pydantic import BaseModel

from enums import MeasurementUnit

__all__ = ('InventoryStockItem', 'UnitInventoryStockItems')


class InventoryStockItem(BaseModel):
    name: str
    quantity: float
    measurement_unit: MeasurementUnit


class UnitInventoryStockItems(BaseModel):
    unit_name: str
    inventory_stock_items: list[InventoryStockItem]

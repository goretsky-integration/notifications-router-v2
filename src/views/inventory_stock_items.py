from enums import MeasurementUnit
from models import UnitInventoryStockItems
from views.base import View

__all__ = ('UnitInventoryStockItemsView',)

MEASUREMENT_UNIT_TO_TEXT = {
    MeasurementUnit.QUANTITY: 'шт',
    MeasurementUnit.KILOGRAM: 'кг',
    MeasurementUnit.LITER: 'л',
    MeasurementUnit.METER: 'м',
}


class UnitInventoryStockItemsView(View):

    def __init__(self, unit_inventory_stock_items: UnitInventoryStockItems):
        self.__unit_inventory_stock_items = unit_inventory_stock_items

    def get_text(self) -> str:
        inventory_stock_items = self.__unit_inventory_stock_items.inventory_stock_items

        lines = [f'<b>{self.__unit_inventory_stock_items.unit_name}</b>']

        if inventory_stock_items:
            lines.append('❗️ <b>На сегодня не хватит</b> ❗️')
        else:
            lines.append('<b>На сегодня всего достаточно</b>')

        for inventory_stock_item in inventory_stock_items:
            measurement_unit_text = (
                MEASUREMENT_UNIT_TO_TEXT[inventory_stock_item.measurement_unit]
            )
            lines.append(
                f'📍 {inventory_stock_item.name} - остаток'
                f' <b><u>{inventory_stock_item.quantity}'
                f' {measurement_unit_text}</u></b>')

        return '\n'.join(lines)

from models import UnitInventoryStockItems
from views.base import View

__all__ = ('UnitInventoryStockItemsView',)


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
            lines.append(
                f'📍 {inventory_stock_item.name} - остаток'
                f' <b><u>{inventory_stock_item.quantity}'
                f' {inventory_stock_item.measurement_unit}</u></b>')

        return '\n'.join(lines)

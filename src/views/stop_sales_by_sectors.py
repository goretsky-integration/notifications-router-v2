from models import UnitStopSalesBySectors
from views.base import View

__all__ = ('UnitStopSalesBySectorsView',)


class UnitStopSalesBySectorsView(View):

    def __init__(self, unit_stop_sales_by_sectors: UnitStopSalesBySectors):
        self.__unit_stop_sales_by_sectors = unit_stop_sales_by_sectors

    def get_text(self) -> str:
        lines = [f'<b>{self.__unit_stop_sales_by_sectors.unit_name}</b>']
        for stop_sale in self.__unit_stop_sales_by_sectors.stop_sales:
            lines.append(
                f'Сектор: {stop_sale.sector_name}'
                f' - с {stop_sale.started_at:%H:%M}'
            )
        return '\n'.join(lines)

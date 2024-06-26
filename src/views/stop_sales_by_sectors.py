from models import UnitStopSalesBySectors
from sorters import sort_by_started_at_ascending_order
from time_helpers import (
    compute_duration,
    humanize_stop_sale_duration,
    is_urgent,
)
from views.base import View

__all__ = ('UnitStopSalesBySectorsView',)


class UnitStopSalesBySectorsView(View):

    def __init__(self, unit_stop_sales_by_sectors: UnitStopSalesBySectors):
        self.__unit_stop_sales_by_sectors = unit_stop_sales_by_sectors

    def get_text(self) -> str:
        unit_name = self.__unit_stop_sales_by_sectors.unit_name
        stop_sales = self.__unit_stop_sales_by_sectors.stop_sales

        if len(stop_sales) == 1:
            sector_singular_or_plural = 'сектор'
        else:
            sector_singular_or_plural = 'сектора'

        sorted_stop_sales = sort_by_started_at_ascending_order(stop_sales)

        lines = [f'<b>{unit_name} {sector_singular_or_plural} в стопе:</b>']

        for stop_sale in sorted_stop_sales:
            duration = compute_duration(stop_sale.started_at)
            humanized_duration = humanize_stop_sale_duration(duration)

            line = (
                f'{stop_sale.sector_name}'
                f' - {humanized_duration}'
                f' (с {stop_sale.started_at:%H:%M})'
            )
            lines.append(line)

        return '\n'.join(lines)

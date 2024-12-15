import operator
from collections.abc import Iterable

from models import SalesStatistics, UnitSalesStatistics
from text_helpers import int_gaps
from views.base import View

__all__ = (
    'SalesStatisticsView',
    'sort_by_sales_for_today',
)


def sort_by_sales_for_today(
        units: Iterable[UnitSalesStatistics],
) -> list[UnitSalesStatistics]:
    return sorted(
        units,
        key=operator.attrgetter('sales_for_today'),
        reverse=True,
    )


class SalesStatisticsView(View):

    def __init__(self, sales_statistics: SalesStatistics):
        self.__sales_statistics = sales_statistics

    def get_text(self) -> str:
        total = self.__sales_statistics.total
        units = sort_by_sales_for_today(self.__sales_statistics.units)

        lines: list[str] = ['<b>Выручка за сегодня</b>']
        lines += [
            f'{unit_statistics.unit_name}'
            f' | {int_gaps(unit_statistics.sales_for_today)}'
            f' | {unit_statistics.sales_growth_from_week_before_in_percents:+}%'
            for unit_statistics in units
        ]
        lines.append(
            f'<b>Итого: {int_gaps(total.sales_for_today)}'
            f' | {total.sales_growth_from_week_before_in_percents:+}%</b>'
        )

        return '\n'.join(lines)

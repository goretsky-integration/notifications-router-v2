import operator
from collections.abc import Iterable

from models import RevenueStatistics, UnitRevenueStatistics
from text_helpers import int_gaps
from views.base import View

__all__ = (
    'RevenueStatisticsView',
    'sort_units_by_revenue_today',
)


def sort_units_by_revenue_today(
        units: Iterable[UnitRevenueStatistics],
) -> list[UnitRevenueStatistics]:
    return sorted(
        units,
        key=operator.attrgetter('revenue_today'),
        reverse=True,
    )


class RevenueStatisticsView(View):

    def __init__(self, revenue_statistics: RevenueStatistics):
        self.__revenue_statistics = revenue_statistics

    def get_text(self) -> str:
        total = self.__revenue_statistics.total
        units = sort_units_by_revenue_today(self.__revenue_statistics.units)

        lines: list[str] = ['<b>Выручка за сегодня</b>']
        lines += [
            f'{unit.unit_name}'
            f' | {int_gaps(unit.revenue_today)}'
            f' | {unit.growth_from_week_before_in_percents:+}%'
            for unit in units
        ]
        lines.append(
            f'<b>Итого: {int_gaps(total.revenue_today)}'
            f' | {total.growth_from_week_before_in_percents:+}%</b>'
        )

        return '\n'.join(lines)

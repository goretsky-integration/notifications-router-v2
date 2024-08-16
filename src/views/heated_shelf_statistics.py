from collections.abc import Iterable

from enums import ReportErrorCode
from models import UnitHeatedShelfStatistics
from time_helpers import humanize_seconds
from views.base import View

__all__ = (
    'report_error_code_to_text',
    'render_trips_with_one_order_percentage',
    'render_average_heated_shelf_time',
    'HeatedShelfStatisticsView',
)

UnitsHeatedShelfStatistics = Iterable[UnitHeatedShelfStatistics]

report_error_code_to_text: dict[ReportErrorCode, str] = {
    ReportErrorCode.AUTH_ERROR: 'Ошибка авторизации',
    ReportErrorCode.API_ERROR: 'Ошибка Dodo API',
    ReportErrorCode.REPORTS_SERVICE_ERROR: 'Ошибка сервиса отчётов',
}


def render_average_heated_shelf_time(
        unit_statistics: UnitHeatedShelfStatistics,
) -> str:
    if unit_statistics.average_heated_shelf_time_in_seconds is not None:
        return humanize_seconds(
            seconds=unit_statistics.average_heated_shelf_time_in_seconds
        )
    return report_error_code_to_text.get(
        unit_statistics.average_heated_shelf_time_error,
    )


def render_trips_with_one_order_percentage(
        unit_statistics: UnitHeatedShelfStatistics,
) -> str:
    if unit_statistics.trips_with_one_orders_percentage is not None:
        return f'{unit_statistics.trips_with_one_orders_percentage:}%'
    return report_error_code_to_text.get(
        unit_statistics.trips_with_one_orders_error,
    )


class HeatedShelfStatisticsView(View):

    def __init__(
            self,
            units_heated_shelf_statistics: UnitsHeatedShelfStatistics,
    ):
        self.__units_heated_shelf_statistics = tuple(
            units_heated_shelf_statistics,
        )

    def get_text(self) -> str:
        lines: list[str] = ['<b>Время ожидания на полке / 1в1</b>']

        units_statistics = sorted(
            self.__units_heated_shelf_statistics,
            key=lambda unit: unit.average_heated_shelf_time_in_seconds,
            reverse=True,
        )

        for unit_statistics in units_statistics:
            lines.append(
                f'{unit_statistics.unit_name}'
                f'| {render_average_heated_shelf_time(unit_statistics)}'
                f'| {render_trips_with_one_order_percentage(unit_statistics)}'
            )

        return '\n'.join(lines)

from collections.abc import Iterable
from typing import TypeAlias

from filters import filter_has_error_code, filter_no_error_code
from models import UnitDeliverySpeedStatistics
from sorters import sort_by_average_delivery_order_fulfillment_time
from text_helpers import ERROR_CODE_TO_MESSAGE, abbreviate_unit_name
from time_helpers import humanize_seconds
from views.base import View

__all__ = (
    'DeliverySpeedStatisticsView',
    'render_unit_delivery_speed_statistics',
)

UnitsDeliverySpeedStatistics: TypeAlias = Iterable[UnitDeliverySpeedStatistics]


def render_unit_delivery_speed_statistics_error(
        unit_statistics: UnitDeliverySpeedStatistics,
) -> str:
    unit_name = abbreviate_unit_name(unit_statistics.unit_name)
    error_message = ERROR_CODE_TO_MESSAGE[unit_statistics.error_code]
    return f'{unit_name} - {error_message}'


def render_unit_delivery_speed_statistics(
        unit_statistics: UnitDeliverySpeedStatistics,
) -> str:
    unit_name = abbreviate_unit_name(unit_statistics.unit_name)
    average_delivery_order_fulfillment_time_in_seconds = humanize_seconds(
        unit_statistics.average_delivery_order_fulfillment_time_in_seconds,
    )
    average_cooking_time_in_seconds = humanize_seconds(
        unit_statistics.average_cooking_time_in_seconds,
    )
    average_heated_shelf_time_in_seconds = humanize_seconds(
        unit_statistics.average_heated_shelf_time_in_seconds,
    )
    average_order_trip_time_in_seconds = humanize_seconds(
        unit_statistics.average_order_trip_time_in_seconds,
    )
    return (
        f'{unit_name}'
        f' | {average_delivery_order_fulfillment_time_in_seconds}'
        f' | {average_cooking_time_in_seconds}'
        f' | {average_heated_shelf_time_in_seconds}'
        f' | {average_order_trip_time_in_seconds}'
    )


class DeliverySpeedStatisticsView(View):

    def __init__(
            self,
            units_delivery_speed_statistics: UnitsDeliverySpeedStatistics,
    ):
        self.__units_delivery_speed_statistics = units_delivery_speed_statistics

    def get_text(self) -> str:
        lines: list[str] = [
            '<b>'
            'Общая скорость доставки'
            ' - Время приготовления'
            ' - Время на полке'
            ' - Поездка курьера'
            '</b>',
        ]

        units_statistics_without_errors = filter_no_error_code(
            items=self.__units_delivery_speed_statistics,
        )
        units_statistics_with_errors = filter_has_error_code(
            items=self.__units_delivery_speed_statistics,
        )

        sorted_units_statistics_without_errors = (
            sort_by_average_delivery_order_fulfillment_time(
                items=units_statistics_without_errors,
            )
        )

        lines += [
            render_unit_delivery_speed_statistics(unit)
            for unit in sorted_units_statistics_without_errors
        ]
        lines += [
            render_unit_delivery_speed_statistics_error(unit)
            for unit in units_statistics_with_errors
        ]

        return '\n'.join(lines)

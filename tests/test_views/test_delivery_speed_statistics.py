from time_helpers import humanize_seconds
from views.delivery_speed import DeliverySpeedStatisticsView
from tests.factories import UnitDeliverySpeedStatisticsFactory


def test_delivery_speed_statistics_view_single_unit_no_error():
    unit = UnitDeliverySpeedStatisticsFactory(error_code=None)

    view = DeliverySpeedStatisticsView([unit])

    actual = view.get_text()

    average_delivery_order_fulfillment_time_in_seconds = humanize_seconds(
        unit.average_delivery_order_fulfillment_time_in_seconds,
    )
    average_cooking_time_in_seconds = humanize_seconds(
        unit.average_cooking_time_in_seconds,
    )
    average_heated_shelf_time_in_seconds = humanize_seconds(
        unit.average_heated_shelf_time_in_seconds,
    )
    average_order_trip_time_in_seconds = humanize_seconds(
        unit.average_order_trip_time_in_seconds,
    )

    expected = (
        '<b>'
        'Общая скорость доставки'
        ' - Время приготовления'
        ' - Время на полке'
        ' - Поездка курьера'
        '</b>\n'
        f'{unit.unit_name}'
        f' | {average_delivery_order_fulfillment_time_in_seconds}'
        f' | {average_cooking_time_in_seconds}'
        f' | {average_heated_shelf_time_in_seconds}'
        f' | {average_order_trip_time_in_seconds}'
    )
    assert actual == expected

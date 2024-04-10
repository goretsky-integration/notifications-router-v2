import textwrap

from tests.factories import UnitLateDeliveryVouchersFactory
from views.late_delivery_vouchers import (
    render_late_delivery_vouchers,
    sort_late_delivery_vouchers,
)


def test_sort_late_delivery_vouchers() -> None:
    unsorted_vouchers = [
        UnitLateDeliveryVouchersFactory(
            certificates_count_today=0,
            certificates_count_week_before=0,
        ),
        UnitLateDeliveryVouchersFactory(
            certificates_count_today=5,
            certificates_count_week_before=3,
        ),
        UnitLateDeliveryVouchersFactory(
            certificates_count_today=2,
            certificates_count_week_before=1,
        ),
        UnitLateDeliveryVouchersFactory(
            certificates_count_today=2,
            certificates_count_week_before=3,
        ),
    ]
    expected = [
        unsorted_vouchers[1],
        unsorted_vouchers[3],
        unsorted_vouchers[2],
        unsorted_vouchers[0],
    ]
    actual = sort_late_delivery_vouchers(unsorted_vouchers)
    assert actual == expected


def test_render_late_delivery_vouchers() -> None:
    unit_vouchers = UnitLateDeliveryVouchersFactory()

    expected = textwrap.dedent(f"""\
        <b>Сертификаты за опоздание (сегодня) | (неделю назад)</b>
        {unit_vouchers.unit_name} | {unit_vouchers.certificates_count_today} шт | {unit_vouchers.certificates_count_week_before} шт""")

    actual = render_late_delivery_vouchers([unit_vouchers])

    assert actual == expected

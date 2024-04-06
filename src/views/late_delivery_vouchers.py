from collections.abc import Iterable

from models import UnitLateDeliveryVouchers

__all__ = (
    'sort_late_delivery_vouchers',
    'render_late_delivery_vouchers',
)


def sort_late_delivery_vouchers(
        units_late_delivery_vouchers: Iterable[UnitLateDeliveryVouchers],
) -> list[UnitLateDeliveryVouchers]:
    return sorted(
        units_late_delivery_vouchers,
        reverse=True,
        key=lambda unit: (
            unit.certificates_count_today,
            unit.certificates_count_week_before,
        ),
    )


def render_late_delivery_vouchers(
        units_late_delivery_vouchers: Iterable[UnitLateDeliveryVouchers],
):
    lines = ['<b>Сертификаты за опоздание (сегодня) | (неделю назад)</b>']

    units_vouchers = sort_late_delivery_vouchers(units_late_delivery_vouchers)

    for unit in units_vouchers:
        lines.append(
            f'{unit.unit_name}'
            f' | {unit.certificates_count_today} шт'
            f' | {unit.certificates_count_week_before} шт'
        )

    return '\n'.join(lines)

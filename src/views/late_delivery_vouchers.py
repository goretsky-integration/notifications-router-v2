from collections.abc import Iterable
from typing import TypeAlias

from models import UnitLateDeliveryVouchers
from views.base import View

__all__ = (
    'sort_late_delivery_vouchers',
    'LateDeliveryVouchersView',
)

UnitsLateDeliveryVouchers: TypeAlias = Iterable[UnitLateDeliveryVouchers]


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


class LateDeliveryVouchersView(View):

    def __init__(self, units_late_delivery_vouchers: UnitsLateDeliveryVouchers):
        self.__units_late_delivery_vouchers = units_late_delivery_vouchers

    def get_text(self) -> str:
        lines = ['<b>Сертификаты за опоздание (сегодня) | (неделю назад)</b>']

        units_vouchers = sort_late_delivery_vouchers(
            units_late_delivery_vouchers=self.__units_late_delivery_vouchers,
        )

        for unit in units_vouchers:
            lines.append(
                f'{unit.unit_name}'
                f' | {unit.certificates_count_today} шт'
                f' | {unit.certificates_count_week_before} шт'
            )

        return '\n'.join(lines)

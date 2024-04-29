import operator
from collections.abc import Iterable
from typing import Final
from uuid import UUID

from enums import CountryCode, SalesChannel
from models import CanceledOrder, UnitCanceledOrders
from views.base import View

__all__ = (
    'UnitCanceledOrdersView',
    'build_order_url',
    'compute_total_price',
    'SALES_CHANNEL_TO_NAME',
    'render_canceled_orders',
    'render_canceled_order',
)

SALES_CHANNEL_TO_NAME: Final[dict[SalesChannel, str]] = {
    SalesChannel.DINE_IN: 'Ресторан',
    SalesChannel.TAKEAWAY: 'Самовывоз',
    SalesChannel.DELIVERY: 'Доставка',
}

COUNTRY_CODE_TO_CURRENCY_SYMBOL: Final[dict[CountryCode, str]] = {
    CountryCode.RU: '₽',
}


def build_order_url(
        *,
        country_code: CountryCode,
        order_id: UUID,
) -> str:
    return (
        f'https://shiftmanager.dodopizza.{country_code}'
        f'/Managment/ShiftManagment/Order?orderUUId={order_id.hex}'
    )


def compute_total_price(orders: Iterable[CanceledOrder]) -> int:
    return sum(order.price for order in orders)


def sort_orders_by_printed_receipt(
        orders: Iterable[CanceledOrder],
) -> list[CanceledOrder]:
    return sorted(
        orders,
        key=operator.attrgetter('has_printed_receipt'),
        reverse=True,
    )


def render_canceled_order(
        *,
        order: CanceledOrder,
        country_code: CountryCode,
        currency_symbol: str,
) -> str:
    lines: list[str] = []

    order_url = build_order_url(
        country_code=country_code,
        order_id=order.id,
    )

    if not order.has_printed_receipt:
        lines.append('<b>❗️ Пока без чека ❗️</b>')

    lines.append(
        f'Заказ <a href="{order_url}">№{order.number}</a>'
        f' {order.price}{currency_symbol}'
    )
    lines.append(
        f'Тип заказа: {SALES_CHANNEL_TO_NAME[order.sales_channel]}'
    )
    return '\n'.join(lines)


def render_canceled_orders(
        *,
        orders: Iterable[CanceledOrder],
        country_code: CountryCode,
        currency_symbol: str,
) -> str:
    lines = [
        render_canceled_order(
            order=order,
            country_code=country_code,
            currency_symbol=currency_symbol,
        )
        for order in orders
    ]
    return f'\n\n'.join(lines)


class UnitCanceledOrdersView(View):

    def __init__(self, unit_canceled_orders: UnitCanceledOrders):
        self.__unit_canceled_orders = unit_canceled_orders

    def get_text(self) -> str:
        country_code = self.__unit_canceled_orders.country_code
        currency_symbol = COUNTRY_CODE_TO_CURRENCY_SYMBOL.get(country_code, '')

        orders = sort_orders_by_printed_receipt(
            orders=self.__unit_canceled_orders.orders,
        )
        orders_text = render_canceled_orders(
            orders=orders,
            country_code=country_code,
            currency_symbol=currency_symbol,
        )
        total_price = compute_total_price(self.__unit_canceled_orders.orders)

        return (
            f'<b>Отчёт по отменам {self.__unit_canceled_orders.unit_name}:</b>'
            '\n\n'
            f'{orders_text}'
            '\n\n'
            f'<b>Итого: {total_price}{currency_symbol}</b>'
        )

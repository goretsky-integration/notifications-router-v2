from datetime import datetime

from enums import SalesChannel
from models import StopSaleBySalesChannel
from time_helpers import (
    compute_duration,
    humanize_stop_sale_duration,
    is_urgent,
)
from views.base import View

SALES_CHANNEL_TO_NAME = {
    SalesChannel.DINE_IN: 'Ресторан',
    SalesChannel.TAKEAWAY: 'Самовывоз',
    SalesChannel.DELIVERY: 'Доставка',
}

__all__ = (
    'render_stop_sale_header',
    'StopSaleBySalesChannelView',
    'SALES_CHANNEL_TO_NAME',
)


def render_stop_sale_header(
        *,
        unit_name: str,
        started_at: datetime,
):
    stop_sale_duration = compute_duration(started_at)
    humanized_stop_sale_duration = humanize_stop_sale_duration(
        duration=stop_sale_duration,
    )
    humanized_stop_sale_started_at = f'{started_at:%H:%M}'

    header = (
        f'{unit_name}'
        f' в стопе {humanized_stop_sale_duration}'
        f' (с {humanized_stop_sale_started_at})')

    if is_urgent(stop_sale_duration):
        header = '❗️ ' + header + ' ❗️'

    return header


class StopSaleBySalesChannelView(View):

    def __init__(self, stop_sale: StopSaleBySalesChannel):
        self.__stop_sale = stop_sale

    def get_text(self) -> str:
        header = render_stop_sale_header(
            unit_name=self.__stop_sale.unit_name,
            started_at=self.__stop_sale.started_at,
        )
        channel_name = SALES_CHANNEL_TO_NAME[self.__stop_sale.sales_channel]
        return (
            f'{header}\n'
            f'Тип продажи: {channel_name}\n'
            f'Причина: {self.__stop_sale.reason}'
        )

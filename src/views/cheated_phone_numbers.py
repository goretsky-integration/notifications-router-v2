from models import UnitCheatedOrders
from views.base import View

__all__ = ('CheatedPhoneNumbersView',)


class CheatedPhoneNumbersView(View):

    def __init__(self, unit_cheated_orders: UnitCheatedOrders):
        self.__unit_cheated_orders = unit_cheated_orders

    def get_text(self) -> str:
        lines: list[str] = [
            '<b>❗️ ПОДОЗРИТЕЛЬНО 🤨 ❗️️',
            f'{self.__unit_cheated_orders.unit_name}</b>',
            f'Номер: {self.__unit_cheated_orders.phone_number}',
        ]

        for order in self.__unit_cheated_orders.orders:
            lines.append(
                f'{order.created_at:%H:%M} - <b>заказ №{order.number}</b>'
            )

        return '\n'.join(lines)

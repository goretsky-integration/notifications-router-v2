from models import UnitUnprintedReceipts
from text_helpers import int_gaps
from views.base import View

__all__ = ('UnitUnprintedReceiptsView',)


class UnitUnprintedReceiptsView(View):

    def __init__(self, unit_unprinted_receipts: UnitUnprintedReceipts):
        self.__unit_unprinted_receipts = unit_unprinted_receipts

    def get_text(self) -> str:
        unit_name = self.__unit_unprinted_receipts.unit_name
        orders = self.__unit_unprinted_receipts.orders

        lines: list[str] = [
            'Менеджер, привет!',
            f'<b>В пиццерии {unit_name} есть незакрытые чеки,</b>'
            ' пожалуйста, проверь информацию и закрой все чеки:'
        ]

        for order in orders:
            lines.append(f'{order.number} / {int_gaps(order.price)}')

        return '\n'.join(lines)

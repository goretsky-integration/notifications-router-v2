from factories import UnitCheatedOrdersFactory
from views import CheatedPhoneNumbersView


def test_get_text():
    unit_cheated_orders = UnitCheatedOrdersFactory()
    view = CheatedPhoneNumbersView(unit_cheated_orders)
    result = view.get_text()

    assert '<b>❗️ ПОДОЗРИТЕЛЬНО 🤨 ❗️️' in result
    assert f'{unit_cheated_orders.unit_name}</b>' in result
    assert f'Номер: {unit_cheated_orders.phone_number}' in result

    for order in unit_cheated_orders.orders:
        assert f'{order.created_at:%H:%M} - <b>заказ №{order.number}</b>' in result

from datetime import datetime

import factory

from models.cheated_phone_numbers import CheatedOrder, UnitCheatedOrders

__all__ = ('CheatedOrderFactory', 'UnitCheatedOrdersFactory')


class CheatedOrderFactory(factory.Factory):
    class Meta:
        model = CheatedOrder

    created_at = factory.LazyFunction(datetime.now)
    number = factory.Sequence(lambda n: f'ORDER{n:03d}')


class UnitCheatedOrdersFactory(factory.Factory):
    class Meta:
        model = UnitCheatedOrders

    unit_name = factory.Faker('company')
    phone_number = factory.Faker('phone_number')
    orders = factory.List(
        [factory.SubFactory(CheatedOrderFactory) for _ in range(3)])

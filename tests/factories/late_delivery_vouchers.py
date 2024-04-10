import factory

from models.late_delivery_vouchers import UnitLateDeliveryVouchers

__all__ = ('UnitLateDeliveryVouchersFactory',)


class UnitLateDeliveryVouchersFactory(factory.Factory):
    class Meta:
        model = UnitLateDeliveryVouchers

    unit_name = factory.Faker('city')
    certificates_count_today = factory.Faker(
        'pyint',
        min_value=0,
        max_value=10,
    )
    certificates_count_week_before = factory.Faker(
        'pyint',
        min_value=0,
        max_value=10,
    )

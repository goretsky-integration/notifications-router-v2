import factory

from models.delivery_speed import UnitDeliverySpeedStatistics

__all__ = ('UnitDeliverySpeedStatisticsFactory',)


class UnitDeliverySpeedStatisticsFactory(factory.Factory):
    class Meta:
        model = UnitDeliverySpeedStatistics

    unit_name = factory.Faker('city')
    average_cooking_time_in_seconds = factory.Faker(
        'pyint',
        min_value=0,
        max_value=1000,
    )
    average_delivery_order_fulfillment_time_in_seconds = factory.Faker(
        'pyint',
        min_value=0,
        max_value=1000,
    )
    average_heated_shelf_time_in_seconds = factory.Faker(
        'pyint',
        min_value=0,
        max_value=1000,
    )
    average_order_trip_time_in_seconds = factory.Faker(
        'pyint',
        min_value=0,
        max_value=1000,
    )
    error_code = factory.Faker('word')

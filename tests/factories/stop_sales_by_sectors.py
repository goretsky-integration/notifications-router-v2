import factory

from models.stop_sales_by_sectors import (
    StopSaleBySector,
    UnitStopSalesBySectors,
)


class StopSaleBySectorFactory(factory.Factory):
    class Meta:
        model = StopSaleBySector

    sector_name = factory.Faker('city')
    started_at = factory.Faker('date_time')


class UnitStopSalesBySectorsFactory(factory.Factory):
    class Meta:
        model = UnitStopSalesBySectors

    unit_name = factory.Faker('city')
    stop_sales = factory.List([
        factory.SubFactory(StopSaleBySectorFactory) for _ in range(5)
    ])

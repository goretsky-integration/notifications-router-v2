import factory

from models.revenue import (
    RevenueStatistics,
    TotalRevenueStatistics,
    UnitRevenueStatistics,
)

__all__ = (
    'TotalRevenueStatisticsFactory',
    'RevenueStatisticsFactory',
    'UnitRevenueStatisticsFactory',
)


class TotalRevenueStatisticsFactory(factory.Factory):
    class Meta:
        model = TotalRevenueStatistics

    revenue_today = factory.Faker('pyint', min_value=0, max_value=10_000)
    growth_from_week_before_in_percents = factory.Faker(
        'pyint', min_value=-100, max_value=100,
    )


class UnitRevenueStatisticsFactory(factory.Factory):
    class Meta:
        model = UnitRevenueStatistics

    unit_name = factory.Faker('city')
    revenue_today = factory.Faker('pyint', min_value=0, max_value=10_000)
    growth_from_week_before_in_percents = factory.Faker(
        'pyint', min_value=-100, max_value=100,
    )


class RevenueStatisticsFactory(factory.Factory):
    class Meta:
        model = RevenueStatistics

    units = factory.List([UnitRevenueStatisticsFactory() for _ in range(3)])
    total = factory.SubFactory(TotalRevenueStatisticsFactory)

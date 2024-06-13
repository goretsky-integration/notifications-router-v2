import factory

from models import Unit

__all__ = ('UnitFactory',)


class UnitFactory(factory.Factory):
    class Meta:
        model = Unit

    id = factory.Faker('pyint', min_value=1, max_value=1000)
    name = factory.Faker('city')
    uuid = factory.Faker('uuid4')

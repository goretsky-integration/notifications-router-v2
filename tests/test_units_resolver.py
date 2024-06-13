import pytest

from factories import UnitFactory
from models import Unit
from units_resolver import resolve_unit_ids


@pytest.fixture
def units() -> list[Unit]:
    return UnitFactory.build_batch(size=10)


def test_resolve_unit_ids_int(units) -> None:
    unit_ids = [unit.id for unit in units]

    actual = resolve_unit_ids(units=units, unit_ids=unit_ids)

    expected = {unit.id for unit in units}
    assert actual == expected


def test_resolve_unit_ids_str(units) -> None:
    unit_ids = [unit.name for unit in units]

    actual = resolve_unit_ids(units=units, unit_ids=unit_ids)

    expected = {unit.id for unit in units}
    assert actual == set(expected)


def test_resolve_unit_ids_uuid(units) -> None:
    unit_ids = [unit.uuid for unit in units]

    actual = resolve_unit_ids(units=units, unit_ids=unit_ids)

    expected = {unit.id for unit in units}
    assert actual == set(expected)


def test_resolve_unit_ids_mixed(units) -> None:
    unit_ids = (
            [unit.id for unit in units[:3]]
            + [unit.name for unit in units[3:6]]
            + [unit.uuid for unit in units[6:]]
    )

    actual = resolve_unit_ids(units=units, unit_ids=unit_ids)

    expected = {unit.id for unit in units}
    assert actual == set(expected)


def test_resolve_unit_ids_empty(units) -> None:
    unit_ids = []

    actual = resolve_unit_ids(units=units, unit_ids=unit_ids)

    assert actual == set()


def test_resolve_unit_ids_no_units() -> None:
    units: list[Unit] = []
    unit_ids = [1, 2, 3]

    actual = resolve_unit_ids(units=units, unit_ids=unit_ids)

    assert actual == set()


if __name__ == '__main__':
    pytest.main()

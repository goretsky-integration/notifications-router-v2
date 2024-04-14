import textwrap

import pytest

from factories import StopSaleBySectorFactory, UnitStopSalesBySectorsFactory
from views.stop_sales_by_sectors import UnitStopSalesBySectorsView


def test_unit_stop_sales_by_sectors_view_get_text_with_single_stop_sale():
    stop_sale = StopSaleBySectorFactory()

    unit_stop_sales_by_sectors = UnitStopSalesBySectorsFactory(
        stop_sales=[stop_sale],
    )
    view = UnitStopSalesBySectorsView(unit_stop_sales_by_sectors)

    actual = view.get_text()
    expected = textwrap.dedent(f'''\
    <b>{unit_stop_sales_by_sectors.unit_name}</b>
    Сектор: {stop_sale.sector_name} - с {stop_sale.started_at:%H:%M}''')

    assert actual == expected


def test_unit_stop_sales_by_sectors_view_get_text_with_multiple_stop_sales():
    stop_sale_1 = StopSaleBySectorFactory()
    stop_sale_2 = StopSaleBySectorFactory()
    stop_sale_3 = StopSaleBySectorFactory()

    unit_stop_sales_by_sectors = UnitStopSalesBySectorsFactory(
        stop_sales=[stop_sale_1, stop_sale_2, stop_sale_3],
    )
    view = UnitStopSalesBySectorsView(unit_stop_sales_by_sectors)

    actual = view.get_text()
    expected = textwrap.dedent(f'''\
    <b>{unit_stop_sales_by_sectors.unit_name}</b>
    Сектор: {stop_sale_1.sector_name} - с {stop_sale_1.started_at:%H:%M}
    Сектор: {stop_sale_2.sector_name} - с {stop_sale_2.started_at:%H:%M}
    Сектор: {stop_sale_3.sector_name} - с {stop_sale_3.started_at:%H:%M}''')

    assert actual == expected


if __name__ == '__main__':
    pytest.main()

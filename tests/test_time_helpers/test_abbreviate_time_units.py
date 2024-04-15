import pytest

from time_helpers import abbreviate_time_units


@pytest.mark.parametrize(
    'input_text, expected_output',
    [
        ('1 дн 2 ч 3 мин', '1 дн 2 ч 3 мин'),
        ('24 ч 10 мин', '24 ч 10 мин'),
        ('1 день 2 часа 3 минуты', '1 дн 2 ч 3 мин'),
        ('30 минут', '30 мин'),
        ('полчаса', 'полчаса'),
        ('', ''),
    ]
)
def test_abbreviate_time_units(input_text, expected_output):
    assert abbreviate_time_units(input_text) == expected_output

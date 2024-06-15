from models import StopSaleByIngredient, UnitStopSalesByIngredients
from sorters import sort_by_created_at_descending_order
from time_helpers import compute_duration, humanize_stop_sale_duration
from views.base import View

__all__ = ('UnitStopSalesByIngredientsView', 'render_stop_sale_by_ingredient',)


def render_stop_sale_by_ingredient(stop_sale: StopSaleByIngredient) -> str:
    duration = compute_duration(stop_sale.started_at)
    humanized_stop_duration = humanize_stop_sale_duration(duration)
    return (
        f'📍 {stop_sale.ingredient_name}'
        f' - <b><u>{humanized_stop_duration}</u></b>'
    )


class UnitStopSalesByIngredientsView(View):

    def __init__(
            self,
            unit_stop_sales_by_ingredients: UnitStopSalesByIngredients,
    ):
        self.__unit_stop_sales_by_ingredients = unit_stop_sales_by_ingredients

    def get_text(self) -> str:
        lines = [f'<b>{self.__unit_stop_sales_by_ingredients.unit_name}</b>']

        stop_sales_by_reasons = self.__unit_stop_sales_by_ingredients.stop_sales_grouped_by_reasons

        if not stop_sales_by_reasons:
            lines.append(
                '<b>Стопов пока нет!'
                ' Молодцы. Ваши Клиенты довольны</b>'
            )

        for stop_sales_by_reason in stop_sales_by_reasons:
            stop_sales = sort_by_created_at_descending_order(
                stop_sales_by_reason.stop_sales,
            )

            lines.append(f'\n<b>{stop_sales_by_reason.reason}:</b>')
            lines += [
                render_stop_sale_by_ingredient(stop_sale)
                for stop_sale in stop_sales
            ]
        return '\n'.join(lines)

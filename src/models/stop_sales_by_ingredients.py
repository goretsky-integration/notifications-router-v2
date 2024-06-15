from datetime import datetime

from pydantic import BaseModel, conlist

__all__ = (
    'StopSalesByIngredientsGroupedByReason',
    'StopSaleByIngredient',
    'UnitStopSalesByIngredients',
)


class StopSaleByIngredient(BaseModel):
    started_at: datetime
    ingredient_name: str


class StopSalesByIngredientsGroupedByReason(BaseModel):
    reason: str
    stop_sales: conlist(StopSaleByIngredient, min_length=1)


class UnitStopSalesByIngredients(BaseModel):
    unit_name: str
    stop_sales_grouped_by_reasons: list[StopSalesByIngredientsGroupedByReason]

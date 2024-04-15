from datetime import datetime

from pydantic import BaseModel, conlist

__all__ = ('UnitStopSalesByIngredients', 'StopSaleByIngredient')


class StopSaleByIngredient(BaseModel):
    started_at: datetime
    reason: str
    ingredient_name: str


class UnitStopSalesByIngredients(BaseModel):
    unit_name: str
    stops_sales: conlist(StopSaleByIngredient, min_length=1)

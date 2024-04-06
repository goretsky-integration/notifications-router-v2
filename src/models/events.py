from typing import Any
from uuid import UUID

from pydantic import BaseModel

from enums import SpecificChatsEventType

__all__ = (
    'GlobalEvent',
    'SpecificChatsEvent',
    'SpecificUnitsEvent',
)


class GlobalEvent(BaseModel):
    type: str
    payload: Any


class SpecificUnitsEvent(BaseModel):
    type: str
    payload: Any
    unit_ids: set[UUID]


class SpecificChatsEvent(BaseModel):
    type: SpecificChatsEventType
    payload: Any
    chat_ids: set[int]

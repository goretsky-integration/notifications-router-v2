from typing import Any
from uuid import UUID

from pydantic import BaseModel

from enums import EventType

__all__ = (
    'GlobalEvent',
    'SpecificChatsEvent',
    'SpecificUnitsEvent',
)


class GlobalEvent(BaseModel):
    type: EventType
    payload: Any


class SpecificUnitsEvent(BaseModel):
    type: EventType
    payload: Any
    unit_ids: set[int]


class SpecificChatsEvent(BaseModel):
    type: EventType
    payload: Any
    chat_ids: set[int]

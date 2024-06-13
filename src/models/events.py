from typing import Any, TypeAlias
from uuid import UUID

from pydantic import BaseModel

from enums import EventType

__all__ = (
    'GlobalEvent',
    'SpecificChatsEvent',
    'SpecificUnitsEvent',
    'UnitIdOrNameOrUUID',
)

UnitIdOrNameOrUUID: TypeAlias = int | str | UUID


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

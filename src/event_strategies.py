from typing import Any, Protocol, TypedDict

from pydantic import BaseModel, TypeAdapter

from enums import EventType
from models import UnitInventoryStockItems, UnitLateDeliveryVouchers, WriteOff
from views import (
    LateDeliveryVouchersView,
    UnitInventoryStockItemsView,
    WriteOffView,
)
from views.base import View

__all__ = (
    'SPECIFIC_CHATS_EVENT_STRATEGIES',
    'serialize_and_get_view',
)


class ReceivesArbitraryArguments(Protocol):

    def __init__(self, *args, **kwargs): ...


class SpecificChatsEventStrategy(TypedDict):
    view: type[View | ReceivesArbitraryArguments]
    model: BaseModel | TypeAdapter


SPECIFIC_CHATS_EVENT_STRATEGIES: (
    dict[EventType, SpecificChatsEventStrategy]
) = {
    EventType.LATE_DELIVERY_VOUCHERS: {
        'view': LateDeliveryVouchersView,
        'model': TypeAdapter(list[UnitLateDeliveryVouchers]),
    },
    EventType.WRITE_OFFS: {
        'view': WriteOffView,
        'model': WriteOff,
    },
    EventType.STOPS_AND_RESUMES: {
        'view': UnitInventoryStockItemsView,
        'model': UnitInventoryStockItems,
    },
}


class HasTypeAndPayload(Protocol):
    type: EventType
    payload: Any


def serialize_and_get_view(event: HasTypeAndPayload) -> View:
    strategy = SPECIFIC_CHATS_EVENT_STRATEGIES[event.type]

    view = strategy['view']
    model = strategy['model']

    if isinstance(model, TypeAdapter):
        payload = model.validate_python(event.payload)
    else:
        payload = model.model_validate(event.payload)

    return view(payload)

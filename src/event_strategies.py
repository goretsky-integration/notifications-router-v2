from collections.abc import Callable
from typing import Any, Protocol, TypeAlias, TypedDict

from pydantic import BaseModel, TypeAdapter

from enums import EventType
from models import UnitLateDeliveryVouchers, WriteOff
from views import render_late_delivery_vouchers, render_write_off

__all__ = (
    'SPECIFIC_CHATS_EVENT_STRATEGIES',
    'serialize_and_render',
)

Renderer: TypeAlias = Callable[[...], str]


class SpecificChatsEventStrategy(TypedDict):
    renderer: Renderer
    model: BaseModel | TypeAdapter


SPECIFIC_CHATS_EVENT_STRATEGIES: (
    dict[EventType, SpecificChatsEventStrategy]
) = {
    EventType.LATE_DELIVERY_VOUCHERS: {
        'renderer': render_late_delivery_vouchers,
        'model': TypeAdapter(list[UnitLateDeliveryVouchers]),
    },
    EventType.WRITE_OFFS: {
        'renderer': render_write_off,
        'model': WriteOff,
    }
}


class HasTypeAndPayload(Protocol):
    type: EventType
    payload: Any


def serialize_and_render(event: HasTypeAndPayload) -> str:
    strategy = SPECIFIC_CHATS_EVENT_STRATEGIES[event.type]

    render = strategy['renderer']
    model = strategy['model']

    if isinstance(model, TypeAdapter):
        payload = model.validate_python(event.payload)
    else:
        payload = model.model_validate(event.payload)

    return render(payload)

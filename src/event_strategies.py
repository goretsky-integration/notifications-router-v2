from collections.abc import Callable
from typing import TypeAlias, TypedDict

from pydantic import BaseModel, TypeAdapter

from enums import SpecificChatsEventType
from models import SpecificChatsEvent, UnitLateDeliveryVouchers
from views import render_late_delivery_vouchers

__all__ = (
    'SPECIFIC_CHATS_EVENT_STRATEGIES',
    'serialize_and_render',
)

Renderer: TypeAlias = Callable[[...], str]


class SpecificChatsEventStrategy(TypedDict):
    renderer: Renderer
    model: BaseModel | TypeAdapter


SPECIFIC_CHATS_EVENT_STRATEGIES: (
    dict[SpecificChatsEventType, SpecificChatsEventStrategy]
) = {
    SpecificChatsEventType.LATE_DELIVERY_VOUCHERS: {
        'renderer': render_late_delivery_vouchers,
        'model': TypeAdapter(list[UnitLateDeliveryVouchers]),
    },
}


def serialize_and_render(event: SpecificChatsEvent) -> str:
    strategy = SPECIFIC_CHATS_EVENT_STRATEGIES[event.type]

    render = strategy['renderer']
    model = strategy['model']

    if isinstance(model, TypeAdapter):
        payload = model.validate_python(event.payload)
    else:
        payload = model.model_validate(event.payload)

    return render(payload)

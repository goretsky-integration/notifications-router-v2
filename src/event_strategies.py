from typing import Any, Protocol, TypedDict

from pydantic import BaseModel, TypeAdapter

from enums import EventType
from models import (
    RevenueStatistics,
    UnitCanceledOrders,
    UnitCheatedOrders,
    UnitDeliverySpeedStatistics,
    UnitInventoryStockItems,
    UnitLateDeliveryVouchers,
    UnitStopSalesByIngredients, WriteOff,
)
from views import (
    CheatedPhoneNumbersView,
    DeliverySpeedStatisticsView,
    LateDeliveryVouchersView,
    RevenueStatisticsView,
    UnitCanceledOrdersView,
    UnitInventoryStockItemsView,
    WriteOffView,
)
from views.base import View

__all__ = (
    'SPECIFIC_CHATS_EVENT_STRATEGIES',
    'serialize_and_get_view',
)

from views.unit_stop_sales_by_ingredients import UnitStopSalesByIngredientsView


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
    EventType.DELIVERY_SPEED: {
        'view': DeliverySpeedStatisticsView,
        'model': TypeAdapter(list[UnitDeliverySpeedStatistics]),
    },
    EventType.STOPS_AND_RESUMES: {
        'view': UnitInventoryStockItemsView,
        'model': UnitInventoryStockItems,
    },
    EventType.CANCELED_ORDERS: {
        'view': UnitCanceledOrdersView,
        'model': UnitCanceledOrders,
    },
    EventType.REVENUE_STATISTICS: {
        'view': RevenueStatisticsView,
        'model': RevenueStatistics,
    },
    EventType.CHEATED_PHONE_NUMBERS: {
        'view': CheatedPhoneNumbersView,
        'model': UnitCheatedOrders,
    },
    EventType.INGREDIENTS_STOP_SALES: {
        'view': UnitStopSalesByIngredientsView,
        'model': UnitStopSalesByIngredients,
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

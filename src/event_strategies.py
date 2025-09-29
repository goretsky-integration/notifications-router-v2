from typing import Any, Protocol, TypedDict

from pydantic import BaseModel, TypeAdapter

from enums import EventType
from models import (
    SalesStatistics,
    StopSaleBySalesChannel,
    UnitCanceledOrders,
    UnitCheatedOrders,
    UnitDeliverySpeedStatistics,
    UnitHeatedShelfStatistics,
    UnitInventoryStockItems,
    UnitLateDeliveryVouchers,
    UnitStopSalesByIngredients,
    UnitStopSalesBySectors,
    UnitUnprintedReceipts,
    WriteOff,
    CustomerFeedback,
)
from views import (
    CheatedPhoneNumbersView,
    DeliverySpeedStatisticsView,
    HeatedShelfStatisticsView,
    LateDeliveryVouchersView,
    SalesStatisticsView,
    StopSaleBySalesChannelView,
    UnitCanceledOrdersView,
    UnitInventoryStockItemsView,
    UnitStopSalesByIngredientsView,
    UnitStopSalesBySectorsView,
    UnitUnprintedReceiptsView,
    WriteOffView,
    CustomerFeedbackView,
)
from views.base import View

__all__ = (
    "SPECIFIC_CHATS_EVENT_STRATEGIES",
    "serialize_and_get_view",
)


class ReceivesArbitraryArguments(Protocol):
    def __init__(self, *args, **kwargs): ...


class SpecificChatsEventStrategy(TypedDict):
    view: type[View | ReceivesArbitraryArguments]
    model: BaseModel | TypeAdapter


SPECIFIC_CHATS_EVENT_STRATEGIES: dict[EventType, SpecificChatsEventStrategy] = {
    EventType.LATE_DELIVERY_VOUCHERS: {
        "view": LateDeliveryVouchersView,
        "model": TypeAdapter(list[UnitLateDeliveryVouchers]),
    },
    EventType.WRITE_OFFS: {
        "view": WriteOffView,
        "model": WriteOff,
    },
    EventType.DELIVERY_SPEED: {
        "view": DeliverySpeedStatisticsView,
        "model": TypeAdapter(list[UnitDeliverySpeedStatistics]),
    },
    EventType.INVENTORY_STOCKS: {
        "view": UnitInventoryStockItemsView,
        "model": UnitInventoryStockItems,
    },
    EventType.CANCELED_ORDERS: {
        "view": UnitCanceledOrdersView,
        "model": UnitCanceledOrders,
    },
    EventType.SALES_STATISTICS: {
        "view": SalesStatisticsView,
        "model": SalesStatistics,
    },
    EventType.CHEATED_PHONE_NUMBERS: {
        "view": CheatedPhoneNumbersView,
        "model": UnitCheatedOrders,
    },
    EventType.INGREDIENTS_STOP_SALES: {
        "view": UnitStopSalesByIngredientsView,
        "model": UnitStopSalesByIngredients,
    },
    EventType.SECTOR_STOP_SALES: {
        "view": UnitStopSalesBySectorsView,
        "model": UnitStopSalesBySectors,
    },
    EventType.PIZZERIA_STOP_SALES: {
        "view": StopSaleBySalesChannelView,
        "model": StopSaleBySalesChannel,
    },
    EventType.UNPRINTED_RECEIPTS: {
        "view": UnitUnprintedReceiptsView,
        "model": UnitUnprintedReceipts,
    },
    EventType.HEATED_SHELF_STATISTICS: {
        "view": HeatedShelfStatisticsView,
        "model": TypeAdapter(list[UnitHeatedShelfStatistics]),
    },
    EventType.FEEDBACKS: {
        "view": CustomerFeedbackView,
        "model": CustomerFeedback,
    },
}


class HasTypeAndPayload(Protocol):
    type: EventType
    payload: Any


def serialize_and_get_view(event: HasTypeAndPayload) -> View:
    strategy = SPECIFIC_CHATS_EVENT_STRATEGIES[event.type]

    view = strategy["view"]
    model = strategy["model"]

    if isinstance(model, TypeAdapter):
        payload = model.validate_python(event.payload)
    else:
        payload = model.model_validate(event.payload)

    return view(payload)

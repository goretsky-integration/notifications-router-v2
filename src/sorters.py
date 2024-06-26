from datetime import datetime
from typing import Protocol, TypeVar

__all__ = (
    'sort_by_created_at_descending_order',
    'sort_by_average_delivery_order_fulfillment_time',
    'sort_by_started_at_ascending_order',
)


class HasCreatedAt(Protocol):
    started_at: datetime


class HasAverageDeliveryOrderFulfillmentTimeInSeconds(Protocol):
    average_delivery_order_fulfillment_time_in_seconds: int


HasStartedAtT = TypeVar('HasStartedAtT', bound=HasCreatedAt)
HasAverageDeliveryOrderFulfillmentTimeInSecondsT = TypeVar(
    'HasAverageDeliveryOrderFulfillmentTimeInSecondsT',
    bound=HasAverageDeliveryOrderFulfillmentTimeInSeconds,
)


def sort_by_created_at_descending_order(
        items: list[HasStartedAtT],
) -> list[HasStartedAtT]:
    return sorted(items, key=lambda item: item.started_at, reverse=True)


def sort_by_started_at_ascending_order(
        items: list[HasStartedAtT],
) -> list[HasStartedAtT]:
    return sorted(items, key=lambda item: item.started_at, reverse=False)


def sort_by_average_delivery_order_fulfillment_time(
        items: list[HasAverageDeliveryOrderFulfillmentTimeInSecondsT],
        *,
        reverse: bool = False,
) -> list[HasAverageDeliveryOrderFulfillmentTimeInSecondsT]:
    return sorted(
        items,
        key=lambda item: (
            item.average_delivery_order_fulfillment_time_in_seconds
        ),
        reverse=reverse,
    )

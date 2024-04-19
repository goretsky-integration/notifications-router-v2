from datetime import datetime
from typing import Protocol, TypeVar

__all__ = ('sort_by_created_at_descending_order',)


class HasCreatedAt(Protocol):
    started_at: datetime


HasStartedAtT = TypeVar('HasStartedAtT', bound=HasCreatedAt)


def get_started_at(item: HasStartedAtT) -> datetime:
    return item.started_at


def sort_by_created_at_descending_order(
        items: list[HasStartedAtT],
) -> list[HasStartedAtT]:
    return sorted(items, key=get_started_at, reverse=True)

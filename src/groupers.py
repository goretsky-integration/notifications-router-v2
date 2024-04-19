import itertools
from collections.abc import Iterable
from typing import Protocol, TypeAlias, TypeVar

__all__ = ('group_by_reason',)


class HasReason(Protocol):
    reason: str


HasReasonT = TypeVar('HasReasonT', bound=HasReason)
GroupedByReasonT: TypeAlias = tuple[str, Iterable[HasReasonT]]


def get_reason(item: HasReasonT) -> str:
    return item.reason


def group_by_reason(
        items: Iterable[HasReasonT],
) -> Iterable[tuple[str, Iterable[HasReasonT]]]:
    return itertools.groupby(items, key=get_reason)

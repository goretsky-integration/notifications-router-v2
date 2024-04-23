from collections.abc import Iterable
from typing import Protocol, TypeVar

__all__ = (
    'filter_has_error_code',
    'filter_no_error_code',
)


class HasErrorCode(Protocol):
    error_code: str | None


HasErrorCodeT = TypeVar('HasErrorCodeT', bound=HasErrorCode)


def filter_has_error_code(
        items: Iterable[HasErrorCodeT],
) -> list[HasErrorCodeT]:
    return [item for item in items if item.error_code is not None]


def filter_no_error_code(
        items: Iterable[HasErrorCodeT],
) -> list[HasErrorCodeT]:
    return [item for item in items if item.error_code is None]

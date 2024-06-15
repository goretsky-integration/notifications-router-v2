from collections.abc import Iterable
from typing import assert_never
from uuid import UUID

import structlog.stdlib

from models import Unit, UnitIdOrUUID

__all__ = ('resolve_unit_ids',)

logger = structlog.stdlib.get_logger('app')


def resolve_unit_ids(
        *,
        unit_ids: UnitIdOrUUID | Iterable[UnitIdOrUUID],
        units: Iterable[Unit],
) -> set[int]:
    allowed_unit_ids = {unit.id for unit in units}
    unit_uuid_to_id = {unit.uuid: unit.id for unit in units}

    try:
        iter(unit_ids)
    except TypeError:
        unit_ids = [unit_ids]

    result: set[int] = set()

    for unit_id in unit_ids:
        match unit_id:
            case int():
                if unit_id in allowed_unit_ids:
                    result.add(unit_id)
            case UUID():
                try:
                    result.add(unit_uuid_to_id[unit_id])
                except KeyError:
                    logger.warning('Unit not found', unit_id=unit_id)
            case _:
                logger.error('Unexpected unit_id type', unit_id=unit_id)
                assert_never(unit_id)

    return result

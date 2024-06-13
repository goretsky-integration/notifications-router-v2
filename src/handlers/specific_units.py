from aiogram import Bot
from fast_depends import Depends
from faststream.rabbit import RabbitRouter

from dependencies import get_telegram_bot, get_units_storage_connection
from event_strategies import serialize_and_get_view
from models import SpecificUnitsEvent
from telegram import broadcast_message
from units_storage import UnitsStorageConnection

__all__ = ('router',)

router = RabbitRouter()


@router.subscriber('specific-units-event')
async def on_specific_units_event(
        event: SpecificUnitsEvent,
        telegram_bot: Bot = Depends(get_telegram_bot, use_cache=True),
        units_storage_connection: UnitsStorageConnection = Depends(
            get_units_storage_connection,
            use_cache=False,
        ),
):
    view = serialize_and_get_view(event)

    for unit_id in event.unit_ids:
        report_type = await units_storage_connection.get_report_type_by_name(
            name=event.type,
        )
        chat_ids = await units_storage_connection.get_routes_telegram_chat_ids(
            unit_id=unit_id,
            report_type_id=report_type.id,
        )
        await broadcast_message(
            bot=telegram_bot,
            chat_ids=chat_ids,
            view=view,
        )

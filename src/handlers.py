from aiogram import Bot
from fast_depends import Depends
from faststream.rabbit import RabbitRouter

from dependencies import get_telegram_bot
from event_strategies import serialize_and_render
from models import GlobalEvent, SpecificChatsEvent, SpecificUnitsEvent

router = RabbitRouter()


@router.subscriber('specific-units-event')
async def on_specific_units_event(
        event: SpecificUnitsEvent,
        telegram_bot: Bot = Depends(get_telegram_bot, use_cache=True),
):
    pass


@router.subscriber('specific-chats-event')
async def on_specific_chats_event(
        event: SpecificChatsEvent,
        telegram_bot: Bot = Depends(get_telegram_bot, use_cache=False),
):
    rendered_text = serialize_and_render(event)

    for chat_id in event.chat_ids:
        await telegram_bot.send_message(
            chat_id=chat_id,
            text=rendered_text,
        )


@router.subscriber('global-event')
async def on_global_event(
        event: GlobalEvent,
        telegram_bot: Bot = Depends(get_telegram_bot, use_cache=True),
):
    pass

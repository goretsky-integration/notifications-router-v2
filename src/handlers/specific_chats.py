from aiogram import Bot
from fast_depends import Depends
from faststream.rabbit import RabbitRouter

from dependencies import get_telegram_bot
from event_strategies import serialize_and_get_view
from models import SpecificChatsEvent
from telegram import broadcast_message

__all__ = ('router',)

router = RabbitRouter()


@router.subscriber('specific-chats-event')
async def on_specific_chats_event(
        event: SpecificChatsEvent,
        telegram_bot: Bot = Depends(get_telegram_bot, use_cache=False),
):
    view = serialize_and_get_view(event)
    await broadcast_message(
        bot=telegram_bot,
        chat_ids=event.chat_ids,
        view=view,
    )

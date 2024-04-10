import asyncio
from collections.abc import Iterable

from aiogram import Bot
from aiogram.exceptions import (
    TelegramNetworkError,
    TelegramRetryAfter,
    TelegramServerError,
)

__all__ = ('try_to_send_message', 'broadcast_message')


async def try_to_send_message(
        bot: Bot,
        chat_id: int,
        text: str,
        *,
        attempts: int = 5
) -> None:
    for _ in range(attempts):
        try:
            await bot.send_message(chat_id, text)
        except TelegramRetryAfter as error:
            await asyncio.sleep(error.retry_after + 1)
        except (TelegramNetworkError, TelegramServerError):
            await asyncio.sleep(1)
        else:
            break


async def broadcast_message(
        bot: Bot,
        chat_ids: Iterable[int],
        text: str,
        *,
        attempts: int = 5
) -> None:
    for chat_id in chat_ids:
        await try_to_send_message(bot, chat_id, text, attempts=attempts)
        # Due to Telegram API limits (30 messages per second)
        await asyncio.sleep(0.5)

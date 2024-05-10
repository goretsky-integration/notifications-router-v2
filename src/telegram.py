import asyncio
from collections.abc import Iterable

import structlog.stdlib
from aiogram import Bot
from aiogram.exceptions import (
    TelegramBadRequest,
    TelegramNetworkError,
    TelegramRetryAfter,
    TelegramServerError,
    TelegramMigrateToChat,
)
from structlog.contextvars import bound_contextvars

from views.base import ReplyMarkup, View

__all__ = ('try_to_send_message', 'broadcast_message')

logger = structlog.stdlib.get_logger('app')


async def try_to_send_message(
        bot: Bot,
        chat_id: int,
        text: str,
        *,
        reply_markup: ReplyMarkup | None = None,
        attempts: int = 5
) -> None:
    with bound_contextvars(text=text, chat_id=chat_id):
        for _ in range(attempts):
            try:
                await bot.send_message(chat_id, text, reply_markup=reply_markup)
            except TelegramBadRequest as error:
                logger.error(
                    'Could not send message: Telegram Bad Request',
                    error_message=str(error),
                )
            except TelegramRetryAfter as error:
                logger.warning(
                    'Could not send message: Telegram Retry After',
                    retry_after=error.retry_after,
                )
                await asyncio.sleep(error.retry_after + 1)
            except TelegramMigrateToChat as error:
                logger.warning(
                    'Could not send message: Telegram Migrate To Chat',
                    migrate_to_chat_id=error.migrate_to_chat_id,
                    from_chat_id=chat_id,
                )
            except (TelegramNetworkError, TelegramServerError):
                logger.warning(
                    'Could not send message:'
                    ' Telegram Network Error or Server Error',
                    retry_after=error.retry_after,
                )
                await asyncio.sleep(1)
            else:
                logger.info('Message sent')
                break


async def broadcast_message(
        bot: Bot,
        chat_ids: Iterable[int],
        view: View,
        *,
        attempts: int = 5
) -> None:
    text = view.get_text()
    reply_markup = view.get_reply_markup()
    for chat_id in chat_ids:
        await try_to_send_message(
            bot,
            chat_id,
            text,
            reply_markup=reply_markup,
            attempts=attempts,
        )
        # Due to Telegram API limits (30 messages per second)
        await asyncio.sleep(0.5)

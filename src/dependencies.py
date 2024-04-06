from aiogram import Bot
from aiogram.enums import ParseMode
from fast_depends import Depends

from config import Config, get_config

__all__ = ('get_telegram_bot',)


async def get_telegram_bot(
        config: Config = Depends(get_config, use_cache=True),
) -> Bot:
    bot = Bot(
        token=config.telegram_bot_token.get_secret_value(),
        parse_mode=ParseMode.HTML,
    )
    async with bot.context() as auto_closing_bot:
        yield auto_closing_bot

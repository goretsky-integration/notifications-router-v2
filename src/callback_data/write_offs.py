from uuid import UUID

from aiogram.filters.callback_data import CallbackData

__all__ = ('WriteOffCallbackData',)


class WriteOffCallbackData(CallbackData, prefix='write-off'):
    write_off_id: UUID

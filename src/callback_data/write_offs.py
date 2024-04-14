from aiogram.filters.callback_data import CallbackData

__all__ = ('WriteOffCallbackData',)


class WriteOffCallbackData(CallbackData, prefix='write-off'):
    unit_name: str
    checkbox_a1_coordinates: str

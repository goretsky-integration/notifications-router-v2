from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from callback_data import WriteOffCallbackData
from enums import WriteOffType
from models import WriteOff
from views.base import View

__all__ = ('WriteOffView',)

write_off_type_to_template = {
    WriteOffType.EXPIRE_AT_15_MINUTES: (
        'Списание ингредиента <b>"{ingredient_name}"</b> через 15 минут'
    ),
    WriteOffType.EXPIRE_AT_10_MINUTES: (
        'Списание ингредиента <b>"{ingredient_name}"</b> через 10 минут'
    ),
    WriteOffType.EXPIRE_AT_5_MINUTES: (
        'Списание ингредиента <b>"{ingredient_name}"</b> через 5 минут'
    ),
    WriteOffType.ALREADY_EXPIRED: (
        'В пиццерии просрочка ингредиента <b>"{ingredient_name}"</b>'
    ),
}


class WriteOffView(View):

    def __init__(self, write_off: WriteOff):
        self.__write_off = write_off

    def get_text(self) -> str:
        template = write_off_type_to_template[self.__write_off.type]
        event_description = template.format(
            ingredient_name=self.__write_off.ingredient_name,
        )
        return (
            f'<b>❗️ {self.__write_off.unit_name} ❗️</b>\n'
            f'{event_description}'
        )

    def get_reply_markup(self) -> InlineKeyboardMarkup:
        write_off_button_callback_data = WriteOffCallbackData(
            unit_name=self.__write_off.unit_name,
            checkbox_a1_coordinates=self.__write_off.checkbox_a1_coordinates,
        ).pack()
        write_off_button = InlineKeyboardButton(
            text='🗑️ Списать ингредиент',
            callback_data=write_off_button_callback_data,
        )
        return InlineKeyboardMarkup(inline_keyboard=[[write_off_button]])

from enums import WriteOffType
from models import WriteOff

__all__ = ('render_write_off',)

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


def render_write_off(write_off: WriteOff) -> str:
    template = write_off_type_to_template[write_off.type]
    event_description = template.format(
        ingredient_name=write_off.ingredient_name,
    )
    return (
        f'<b>❗️ {write_off.unit_name} ❗️</b>\n'
        f'{event_description}'
    )

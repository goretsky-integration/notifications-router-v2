from pydantic import BaseModel

from enums import WriteOffType

__all__ = ('WriteOff',)


class WriteOff(BaseModel):
    unit_name: str
    type: WriteOffType
    ingredient_name: str

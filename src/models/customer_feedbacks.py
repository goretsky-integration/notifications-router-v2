import datetime

from pydantic import BaseModel


class CustomerFeedback(BaseModel):
    unit_name: str
    order_number: int
    order_created_at: datetime.datetime
    order_rate: int
    feedback_created_at: datetime.datetime
    feedback_comment: str

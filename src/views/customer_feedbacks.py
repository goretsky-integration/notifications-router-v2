from views.base import View
from models.customer_feedbacks import CustomerFeedback


class CustomerFeedbackView(View):
    def __init__(self, feedback: CustomerFeedback):
        self.__feedback = feedback

    def get_text(self):
        exclamation = "❗️ " if self.__feedback.order_rate == 2 else ""
        return (
            "<b>✍️ Тикеты/Отзывы с комментариями</b>\n"
            f"Время отзыва: {self.__feedback.feedback_created_at:%d.%m.%Y %H:%M}\n"
            f"<b>{self.__feedback.unit_name}</b>\n"
            f"<b>Заказ №{self.__feedback.order_number}</b>\n"
            f"Время заказа: <b>{self.__feedback.order_created_at:%d.%m.%Y %H:%M}</b>\n"
            f"Оценка: <b>{self.__feedback.order_rate}</b> {exclamation}\n"
            f"Комментарий: <b>{self.__feedback.feedback_comment}</b>"
        )

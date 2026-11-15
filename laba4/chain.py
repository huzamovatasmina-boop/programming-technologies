class RequestHandler:
    def __init__(self):
        self._next = None

    def set_next(self, next_handler):
        self._next = next_handler
        return next_handler

    def handle(self, topic: str) -> str:
        if self._next is not None:
            return self._next.handle(topic)
        return "Для этого вопроса обработчик не найден"


class ScheduleHandler(RequestHandler):
    def handle(self, topic: str) -> str:
        if topic == "расписание":
            return "Администратор: занятия по субботам в 11:00"
        return super().handle(topic)


class PaymentHandler(RequestHandler):
    def handle(self, topic: str) -> str:
        if topic == "оплата":
            return "Бухгалтер: оплата занятия перед тренировкой"
        return super().handle(topic)


class TrainerHandler(RequestHandler):
    def handle(self, topic: str) -> str:
        if topic == "тренировка":
            return "Кинолог: начнём с базовых команд"
        return super().handle(topic)


if __name__ == "__main__":
    first = ScheduleHandler()
    second = first.set_next(PaymentHandler())
    second.set_next(TrainerHandler())

    for request in ("расписание", "оплата", "тренировка", "доставка"):
        print(request, "—", first.handle(request))

from dataclasses import dataclass


@dataclass
class TrainingPlan:
    dog_name: str
    goal: str
    exercises: list[str]
    equipment: list[str]
    duration_minutes: int


class TrainingPlanBuilder:
    def __init__(self, dog_name: str):
        self._dog_name = dog_name
        self._goal = ""
        self._exercises = []
        self._equipment = []
        self._duration = 0

    def set_goal(self, goal: str):
        self._goal = goal
        return self

    def add_exercise(self, exercise: str):
        self._exercises.append(exercise)
        return self

    def add_equipment(self, item: str):
        self._equipment.append(item)
        return self

    def set_duration(self, minutes: int):
        self._duration = minutes
        return self

    def build(self) -> TrainingPlan:
        if not self._goal or not self._exercises or self._duration <= 0:
            raise ValueError("Укажите цель, упражнения и длительность")
        return TrainingPlan(
            self._dog_name,
            self._goal,
            self._exercises.copy(),
            self._equipment.copy(),
            self._duration,
        )


if __name__ == "__main__":
    plan = (TrainingPlanBuilder("Рыжик")
            .set_goal("Подготовка к ОКД")
            .add_exercise("Движение рядом")
            .add_exercise("Выдержка")
            .add_equipment("Поводок")
            .set_duration(40)
            .build())

    print("Собака:", plan.dog_name)
    print("Цель:", plan.goal)
    print("Упражнения:", ", ".join(plan.exercises))
    print("Длительность:", plan.duration_minutes, "мин")

from typing import Protocol


class RewardStrategy(Protocol):
    def reward(self, dog_name: str) -> str:
        ...


class FoodReward:
    def reward(self, dog_name: str) -> str:
        return f"{dog_name} получает лакомство"


class ToyReward:
    def reward(self, dog_name: str) -> str:
        return f"{dog_name} играет с мячом"


class TrainingSession:
    def __init__(self, reward_strategy: RewardStrategy):
        self._reward_strategy = reward_strategy

    def set_reward_strategy(self, strategy: RewardStrategy) -> None:
        self._reward_strategy = strategy

    def finish_exercise(self, dog_name: str) -> str:
        return self._reward_strategy.reward(dog_name)


if __name__ == "__main__":
    session = TrainingSession(FoodReward())
    print(session.finish_exercise("Рыжик"))

    session.set_reward_strategy(ToyReward())
    print(session.finish_exercise("Рыжик"))

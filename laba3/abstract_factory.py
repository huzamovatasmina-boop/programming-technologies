from dataclasses import dataclass
from typing import Protocol


@dataclass
class Collar:
    purpose: str
    size: str


@dataclass
class Leash:
    material: str
    length_m: float


class EquipmentFactory(Protocol):
    def create_collar(self) -> Collar:
        ...

    def create_leash(self) -> Leash:
        ...


class CityEquipmentFactory:
    def create_collar(self) -> Collar:
        return Collar("для прогулок", "M")

    def create_leash(self) -> Leash:
        return Leash("нейлон", 2.0)


class SportEquipmentFactory:
    def create_collar(self) -> Collar:
        return Collar("для тренировок", "M")

    def create_leash(self) -> Leash:
        return Leash("биотан", 5.0)


def show_set(factory: EquipmentFactory) -> None:
    collar = factory.create_collar()
    leash = factory.create_leash()
    print(f"Ошейник {collar.purpose}, размер {collar.size}; "
          f"поводок {leash.material}, {leash.length_m} м")


if __name__ == "__main__":
    print("Городской комплект:")
    show_set(CityEquipmentFactory())
    print("Спортивный комплект:")
    show_set(SportEquipmentFactory())

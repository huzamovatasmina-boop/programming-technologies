class ClubSettings:
    """Общие настройки кинологического клуба."""

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.club_name = "Кинологический клуб"
            cls._instance.start_hour = 9
        return cls._instance


if __name__ == "__main__":
    first = ClubSettings()
    second = ClubSettings()

    first.start_hour = 10
    print("Один и тот же объект:", first is second)
    print("Начало занятий:", f"{second.start_hour}:00")

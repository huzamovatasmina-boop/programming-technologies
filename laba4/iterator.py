class TrainingLogIterator:
    def __init__(self, sessions: list[str], reverse: bool = False):
        self._sessions = tuple(sessions)
        self._step = -1 if reverse else 1
        self._position = len(sessions) - 1 if reverse else 0

    def __iter__(self):
        return self

    def __next__(self) -> str:
        if not 0 <= self._position < len(self._sessions):
            raise StopIteration
        session = self._sessions[self._position]
        self._position += self._step
        return session


class TrainingLog:
    def __init__(self):
        self._sessions = []

    def add(self, session: str) -> None:
        self._sessions.append(session)

    def __iter__(self):
        return TrainingLogIterator(self._sessions)

    def reverse_order(self):
        return TrainingLogIterator(self._sessions, reverse=True)


if __name__ == "__main__":
    log = TrainingLog()
    log.add("ОКД — 5 ноября")
    log.add("Выдержка — 7 ноября")
    log.add("Поиск — 10 ноября")

    print("По порядку:")
    for session in log:
        print(session)

    print("В обратном порядке:")
    for session in log.reverse_order():
        print(session)

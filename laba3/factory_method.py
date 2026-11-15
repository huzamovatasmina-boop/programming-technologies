from abc import ABC, abstractmethod


class Lesson(ABC):
    @abstractmethod
    def describe(self) -> str:
        pass


class ObedienceLesson(Lesson):
    def describe(self) -> str:
        return "ОКД: выдержка и движение рядом"


class SearchLesson(Lesson):
    def describe(self) -> str:
        return "Поиск: обнаружение предмета по запаху"


class Course(ABC):
    @abstractmethod
    def create_lesson(self) -> Lesson:
        pass

    def announce(self) -> str:
        lesson = self.create_lesson()
        return f"Занятие: {lesson.describe()}"


class ObedienceCourse(Course):
    def create_lesson(self) -> Lesson:
        return ObedienceLesson()


class SearchCourse(Course):
    def create_lesson(self) -> Lesson:
        return SearchLesson()


if __name__ == "__main__":
    for course in (ObedienceCourse(), SearchCourse()):
        print(course.announce())

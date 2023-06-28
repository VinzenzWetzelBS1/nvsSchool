from datetime import datetime
from course import Course
from student import Student


class Grade:
    def __init__(self, weight: float, date: datetime, level: int, course: Course, student: Student):
        self.__weight = weight
        self.__date = date
        self.set_level(level)
        self.__course = course
        self.__student = student

    def get_weight(self):
        return self.__weight

    def set_weight(self, value: float):
        self.__weight = value

    def get_date(self):
        return self.__date

    def set_date(self, value: datetime):
        self.__date = value

    def get_level(self):
        return self.__level

    def set_level(self, value: int):
        try:
            if value < 1 or value > 6:
                raise ValueError("Der Wert war in keinem gültigen Bereich.")
            else:
                self.__level = value
        except ValueError as e:
            print(e)
        except Exception as e:
            print(f"Unbekannter Fehler. {e}")


    def get_course(self):
        return self.__course

    def set_course(self, value: Course):
        self.__course = value

    def get_student(self):
        return self.__student

    def set_student(self, student: Student):
        self.__student = student

from datetime import datetime
from Course import Course
from Student import Student


class Grade:
    def __init__(self, weight: float, date: datetime, level: float, course: Course, student: Student):
        self.__weight = weight
        self.__date = date
        self.__level = level
        self.__course = course
        self.__student = student

    def get_weight(self):
        return self.__weight

    def set_weight(self, value: float):
        self.__weight = value

    def get_date(self):
        return self.__date

    def set_date(self, value: Datetime):
        self.__date = value

    def get_level(self):
        return self.__level

    def set_level(self, value: float):
        self.__level = value

    def get_course(self):
        return self.__course

    def set_course(self, value: Course):
        self.__course = value

    def get_student(self):
        return self.__student

    def set_student(self, student: Student):
        self.__student = student

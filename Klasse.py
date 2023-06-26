class Klasse:

    students = []

    def __init__(self, name: str, students = []):
        self.__name = name
        self.__students = students

    def set_name(self, name: str):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_students(self, students):
        self.__students = students

    def get_students(self):
        return self.students


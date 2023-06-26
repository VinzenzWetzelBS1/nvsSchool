class Course:
    def __init__(self, name: str):
        self.__name = name

    def set_name(self, value: str):
        self.__name = value

    def get_name(self):
        return self.__name
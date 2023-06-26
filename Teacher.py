from Person import Person


class Teacher(Person):
    def __init__(self, first_name: str, last_name:str):
        super().__init__(first_name, last_name)

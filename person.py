class Person:
    def __init__(self, first_name: str, last_name:str):
        self._first_name = first_name
        self._last_name = last_name

    def set_first_name(self, name:str):
        self._first_name = name

    def get_first_name(self):
        return self._first_name

    def set_last_name(self, name:str):
        self._last_name = name

    def get_last_name(self):
        return self._last_name

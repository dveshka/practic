class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def printName(self):
        return (f"Имя: {self.__name}")

    def printAge(self):
        return (f"Возвраст: {self.__age}")

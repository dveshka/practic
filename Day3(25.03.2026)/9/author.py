class Author:
    name = str
    country = str

    def __init__(self,name,country):
        self.name = name
        self.country = country

    def printInfo(self):
        return (f"ФИО: {self.name}, Страна: {self.country}")


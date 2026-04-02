class Book:
    def __init__(self, bookName):
        self.bookName = bookName
        self.__content =[]
        print(f"Книга с названием: {bookName} создана")
    
    def __del__(self,):
        print(f"Книга с названием: {self.bookName} удалена")

    def addTexts(self, text):
        self.__content.append(text) 
        print(f"Название '{text}', добавлено в содержание книги {self.bookName}")
    
    def checkCount(self):
        print(len(self.__content))  

    def printAllTexts(self):
        for i in range(len(self.__content)):
            print(f"{i + 1}) {self.__content[i]}")
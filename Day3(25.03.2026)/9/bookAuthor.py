import book
import author

class BookAuthor(author.Author, book.Book):
    def __init__(self, name, country, bookName):
        author.Author.__init__(name, country)
        book.Book.__init__(bookName)
    def print(self):
        print(f"ФИО: {self.name}, Страна: {self.country}")
        print(f"Название книги: {self.bookName}")
        for i in range(len(self.__content)):
            print(f"{i + 1}) {self.__content[i]}")
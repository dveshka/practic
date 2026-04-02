import author
import book
import bookAuthor

list = []
author1 = author.Author("Толстой", "Россия")
author2 = author.Author("Турок", "Туркменистан")
author3 = author.Author("Гоголь", "Россия")

list.append(author1)
list.append(author2)
list.append(author3)

print("Все")
for author in list:
    print(author.printInfo())

print("Только из России")
for i in range(len(list)):
    if author.country == "Россия":
        print(author.printInfo())


book1 = book.Book("Супер кНига")
book1.addTexts("как")
book1.addTexts("как2")
book1.addTexts("как3")
book1.checkCount()

book1.printAllTexts()

authorBook = bookAuthor.BookAuthor("Пушкин","Россия","Руслан и Людмила")
authorBook.print()











books = {
    "Книга 1": "автор 1",
    "Книга 2": "автор 2"
}


while True:
    print("1. Просмотр списка книг")
    print("2. Добавить книгу")
    print("3. Удалить книгу")
    print("4. Выход")
    
    x = input("Выберите действие: ")

    if x == "1":
        print("\nСписок книг:")
        for title, author in books.items():
            print(f"«{title}» — {author}")
    if x == "2":
        title = input("Введите название книги: ")
        author = input("Введите автора: ")
        books[title] = author
        print("Книга успешно добавлена")
    if x == "3":
        title = input("Введите название книги для удаления: ")
        try:
            del books[title]
            print(f"Книга «{title}» удалена")
        except KeyError:
            print(f"Книги «{title}» нет ")
    if x == "4":
        print("Выход")
        break
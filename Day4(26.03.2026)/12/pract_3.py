import os.path
from re import match

fileName = input("Введите путь до файла: ")

print("Что сделать с файлом: ")
x = int(input("Вывести на экран: 1\nУдалить файл: 2\nПереименовать файл: 3\nВаш выбор: "))

try:
    if os.path.exists(fileName):
        if x == 1:
            f = open(fileName, 'r')
            text = f.read()
            print(text)
            f.close()
        if x == 2:
            os.remove(fileName)
            print(f"Файл {fileName} был удалён")
        if x == 3:
            newName= input("Введите новое имя: ")
            os.rename(fileName,newName)

    else:
        print(f"Файла {fileName} нет")






except Exception as e:
    print("Ошибка: ", e)
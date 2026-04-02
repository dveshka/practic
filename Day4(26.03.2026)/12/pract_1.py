from logging import exception
import os.path

fileName = input("Введите путь до файла: ")

try:
    f = open(fileName, 'r')
    text = f.read()
    root, ext = os.path.splitext(fileName)
    if ext == ".py":
        exec(text)
    else:
        print(text)


    f.close()
except Exception as e:
    print("Ошибка: ",e)

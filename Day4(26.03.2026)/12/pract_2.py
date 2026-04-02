import os.path

fileName = input("Введите путь до файла: ")

try:
    if os.path.exists(fileName):
        print("Файл существует")
        print("Дописать: 1\nПерезаписать: 2")
        x = int(input("Ваш выбор: "))
        if x == 1:
            f = open(fileName, 'a')
        if x ==2:
            f = open(fileName, 'w')
    else:
        print(f"Файл {fileName} создан")
        f = open(fileName, 'w')


    while(True):
        line = input("Введите строку: ")
        if(line == "end"):
            break
        f.write(f"\n{line}")

    f.close()

except Exception as e:
    print("Ошибка: ",e)
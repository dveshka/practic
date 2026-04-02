import os.path

fileName = "1.txt"

try:
    f = open(fileName, 'r')
    lines = f.readlines()
    print("Первая строка: ",lines[0])
    print("Пятая строка: ",lines[4])
    for i in range(0,5):
        print(f"Строка {i}: ",lines[i] , end= '')

    count = len(lines)

    x = int(input(f"Введите с какой строки начинать(0 - {count}): "))
    y = int(input(f"До какой строки(0 - {count}: "))

    for i in range(x,y+1):
        print(f"Строка {i}: ",lines[i], end= '')

    f.close()
    f = open(fileName, 'r')
    text = f.read()
    print(text)
    f.close()




except Exception as e:
 print("Ошибка: ", e)
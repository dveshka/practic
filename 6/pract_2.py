a = int(input("Введите а: "))
b = int(input("Введите b: "))

while True:
    try:
        res = a / b
        break 
    except ZeroDivisionError:
        print(f"Ошибка: b = {b}, деление невозможно!")
        b = int(input("Введите b: "))
    finally:
        print(f"Результат: {a / b}")
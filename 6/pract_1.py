a = int(input("Введите а: "))
b = int(input("Введите b: "))

try:
    print(a/b)
except ZeroDivisionError:
    print(f"Ошибка: b = {b}, деление не возможно!")

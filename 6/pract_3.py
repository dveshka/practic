import math

try:
    x = float(input("Введите x: "))
    y = float(input("Введите y: "))
    z = float(input("Введите z: "))

    a = x + y + z
    b = (x - y + z)**2

    if a < 0:
        raise ValueError("Корень не извлекается!")

    result = math.sqrt(a) / b
    print(f"Результат выражения: {result}")

except ValueError as msg:
    print(f"Ошибка значения: {msg}")

except ZeroDivisionError:
    print("Ошибка: 0 деление невозможно!")
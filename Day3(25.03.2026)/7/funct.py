def degree( x: "int", a:"int"= 2): 
    """Суперь функция, которая возводит число в степень"""
    if a <= -1:
        print(-1)
    else:
        print(x ** a)

def factorial(x):
    if type(x) != int:
        return -1
    if x == 0 or x == 1:  
        return 1
    if x < 0:
        return -1

    return x * factorial(x - 1) 
          

def allArg(*args):
    sum = 0
    count = 0
    for num in args:
        sum = sum + num
        count = count + 1


    max = args[0]
    min = args[0]
    for num in args:
        if num > max:
            max = num
        if num < min:
            min = num

    print(f"Сумма: {sum}, количество: {count}, макс: {max}, мин: {min}")

    
def multiply(arr, x = 1):
    for i in range(len(arr)):
        arr[i] = arr[i] * x
    return arr

l = lambda a, x, b:  a * x + b

def toSpisok(names, math, ru, inf):
    for i in range(len(names)):
        print(f"{names[i]}: {math[i]}, {ru[i]}, {inf[i]}")



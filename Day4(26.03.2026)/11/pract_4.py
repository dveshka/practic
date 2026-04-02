import re


string = input("Введите пароль: ")


if ((re.search(r"\d",string) != None) &
        (re.search(r"[A-Z]",string) != None) &
        (re.search(r"[a-z]",string) != None) &
        (re.search("\S{6,}",string) != None)):
    print("Пароль сложный")
else:
    print("Пароль лёгкий")




def hello(name = None):
    if name == None:
        print("Hello World")
    else:
        print(f"Hello, {name}")
    
def convert(num, system): 
    str = "" 


def splitText(text):
    t = text.replace(". ", ".")
    text2 = t.split(".")
    for t in text2:
        print(t)

def shifr(text, key = 3):
    alf = "йцукенгшщзхъэждлорпавыфячсмитьбюqwertyuiopasdfghjklzxcvbnm1234567890"
    newText = ""
    for i in range(len(text)):
        n = alf.find(text[i])
        #print(n , text[i])
        newText = newText + alf[n + key]
    print(newText)

def byte(x, y):
    x1 = bin(x).replace("0b","")
    y2 = bin(y).replace("0b","")
    print(x,y)
    print("1 = И, \n2 = ИЛИ, \n3. ИСКЛЮЧАЮЩАЯ ИЛИ, \n4. СДВИГ ВЛЕВО, \n5. СДВИГ ВПРАВО")
    bitOperation = int(input("Выберите битовую операцию: "))
    if bitOperation == 1:
        print(f"{x1}", " И ", f"{y2}", " = ", bin(x & y).replace("0b",""))
    elif bitOperation == 2:
        print(f"{x1}", " ИЛИ ", f"{y2}", " = ", bin(x | y).replace("0b",""))
    elif bitOperation == 3:
        print(f"{x1}", " ИСКЛЮЧАЮЩАЯ ИЛИ ", f"{y2}", " = ", bin(x ^ y).replace("0b",""))
    elif bitOperation == 4:
        print(f"{x1}", " СДВИГ ВЛЕВО ", f"{y2}", " = ", bin(x << y).replace("0b",""))
    elif bitOperation == 5:
        print(f"{x1}", " СДВИГ ВПРАВО ", f"{y2}", " = ", bin(x >> y).replace("0b",""))
    else:
        print("Ошибка")

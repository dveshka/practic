fileName = "555.txt"

try:
    f = open(fileName, 'r')
    lines = f.readlines()

    print(lines)
    for line in lines:
        for part in line:
            string1 = part.s




except Exception as e:
    print("Ошибка: ", e)
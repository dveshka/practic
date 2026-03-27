
question = "Столица России?"
answer = "Россия"

user = input(f"{question}\nВаш ответ: ")
if user.strip().lower() == answer.lower():
    print("Верно! Вы молодец.")
else:
    print(f"Ошибка. Правильный ответ: {answer}")

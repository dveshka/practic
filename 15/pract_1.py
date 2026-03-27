from tkinter import *

def escClose(event: None):
    root.destroy()

def save():
    fileName = "1.txt"

    content = text_widget.get("1.0", END)
    
    with open(fileName, "w", encoding="utf-8") as file:
        file.write(content)
    print("Файл сохранен!")

root = Tk()
root.title("Приложение")
root.geometry("300x250")


text_widget = Text(root, height=10)
text_widget.pack(pady=5)

btn = Button(root, text="Сохранить", command=save)
btn.pack(pady=5)

root.bind("<Escape>", escClose)

root.mainloop()
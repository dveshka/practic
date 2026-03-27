from tkinter import *

def leftClick(event):
    widget = event.widget
    label_text.set(f"Активно: {widget}")

def rightClick(event):
    widget = event.widget
    print(f"Консоль: нажата правая кнопка на {widget}")

root = Tk()
root.title("Приложение")
root.geometry("400x300")

entry1 = Entry(root)
entry1.pack()

entry2 = Entry(root)
entry2.pack()

entry3 = Entry(root)
entry3.pack()


label_text = StringVar(value="Нажмите на поле...")
label = Label(root, textvariable=label_text)
label.pack()

root.bind_class("Entry", "<Button-1>", leftClick)
root.bind_class("Entry", "<Button-3>", rightClick)

root.mainloop()
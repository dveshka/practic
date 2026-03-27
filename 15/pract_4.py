from tkinter import *

def printChar(event):
    new_text = label_keys.cget("text")

    if event.char:
        new_text = new_text + event.char
        label_keys.config(text=new_text)

root = Tk()
root.title("Приложение")
root.geometry("500x200")

label_keys = Label(text="Нажатые клавиши: ")
label_keys.pack()


root.bind("<Key>", printChar)

root.mainloop()
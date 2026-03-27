from tkinter import *

def updateXY(event):
    new_text = f"Мышь: x={event.x}, y={event.y}"
    labelMouse.config(text=new_text)

root = Tk()
root.title("Приложение")
root.geometry("400x300")


labelMouse = Label(
    root, 
    text="Координаты мыши: x=0, y=0",
)
labelMouse.pack(expand=True)

root.bind("<Motion>", updateXY)

root.mainloop()
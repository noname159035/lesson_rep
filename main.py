import tkinter
from tkinter import *
from PIL import Image, ImageTk

window = tkinter.Tk()
window.geometry("370x450")
window.title("Свойства")
window.iconbitmap("img/folder.ico")
window.resizable(False, False)

a = 0
while (a < 10):
    print(a)
    a += 1
    print("я изменил код")

lable_text_top = tkinter.Label(width=40, text="Предыдущие версии можно полчуить из истории")
lable_text_top.place(relx=0.15, rely=0.05)

lable_text_low = tkinter.Label(width=40, text="файлов или точек восстановления")
lable_text_low.place(relx=0.037, rely=0.09)

image = Image.open("img/clock.png")
image = image.resize((30, 30))
photo = ImageTk.PhotoImage(image)

label = tkinter.Label(window, image=photo)
label.image = photo
label.place(relx=0.05, rely=0.05)

lable_text_ver = tkinter.Label(text="Версии файлов")
lable_text_ver.place(relx=0.05, rely=0.18)

listBox = Listbox(width=55, height=16)
listBox.place(relx=0.05, rely=0.25)
listBox.insert(END, "Версия 1")
listBox.insert(END, "Версия 2")
listBox.insert(END, "Версия 3")
listBox.insert(END, "Версия 4")

button_ok = Button(text="Ок")
button_ok.place(relx=0.52, rely=0.90)

button_cancle = Button(text="Отмена")
button_cancle.place(relx=0.60, rely=0.90)

button_apply = Button(text="Применить")
button_apply.place(relx=0.75, rely=0.90)

window.mainloop()

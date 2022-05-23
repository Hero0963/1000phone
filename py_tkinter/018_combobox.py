import tkinter
from tkinter import ttk

win = tkinter.Tk()
win.title("HERO")

win.geometry("400x400+200+20")

cv = tkinter.StringVar()
com = ttk.Combobox(win, textvariable=cv)

com = ttk.Combobox(win)
com.pack()

com["value"] = ("Taipei", "Taichung", "Tainan")

com.current(0)


def func(event):
    print(com.get())


com.bind("<<ComboboxSelected>>", func)

win.mainloop()

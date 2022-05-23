import tkinter

win = tkinter.Tk()
win.title("HERO")

win.geometry("400x400+200+20")


def updata():
    print(v.get())


v = tkinter.StringVar()
v.set(20)

sp = tkinter.Spinbox(win, from_=0, to=100, increment=5, textvariable=v, command=updata)
sp.pack()

win.mainloop()

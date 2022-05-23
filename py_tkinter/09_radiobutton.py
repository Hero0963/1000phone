import tkinter

win = tkinter.Tk()
win.title("HERO")

win.geometry("400x400+200+20")


def updata():
    print(r.get())


r = tkinter.IntVar()

radio1 = tkinter.Radiobutton(win, text="one", value=1, variable=r, command=updata)
radio1.pack()

radio2 = tkinter.Radiobutton(win, text="two", value=2, variable=r, command=updata)
radio2.pack()



win.mainloop()

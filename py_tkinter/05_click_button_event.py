import tkinter

win = tkinter.Tk()
win.title("HERO")

win.geometry("400x400+200+20")


def showInfo():
    print(entry.get())


entry = tkinter.Entry(win)
entry.pack()

button = tkinter.Button(win, text="button", command=showInfo)
button.pack()

win.mainloop()

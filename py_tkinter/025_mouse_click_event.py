import tkinter

win = tkinter.Tk()
win.title("HERO")

win.geometry("400x400+200+20")


def func(event):
    print(event.x, event.y)


# <Button-1> left-mouse
button1 = tkinter.Button(win, text="left-mouse button")
button1.bind("<Button-1>", func)
button1.pack()

win.mainloop()

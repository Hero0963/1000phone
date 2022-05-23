import tkinter

win = tkinter.Tk()
win.title("HERO")

win.geometry("400x400+200+20")

label = tkinter.Label(win, text="hero is a good man", bg="red")
label.pack()


def func(event):
    print(event.x, event.y)


label.bind("<Button-1>", func)

win.mainloop()

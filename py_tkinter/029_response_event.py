import tkinter

win = tkinter.Tk()
win.title("HERO")

win.geometry("400x400+200+20")

label = tkinter.Label(win, text="hero is a good man", bg="red")

label.focus_set()
label.pack()


def func(event):
    print("event.char= ", event.char)
    print("event.keycode= ", event.keycode)


label.bind("<Key>", func)

win.mainloop()

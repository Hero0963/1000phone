import tkinter

win = tkinter.Tk()
win.title("HERO")

win.geometry("400x400+200+20")


def func(event):
    print("event.char= ", event.char)
    print("event.keycode= ", event.keycode)


win.bind("<Control-Alt-a>", func)

win.mainloop()

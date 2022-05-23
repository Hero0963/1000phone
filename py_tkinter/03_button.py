import tkinter


def button1():
    print("hero is a good man")


win = tkinter.Tk()
win.title("HERO")

win.geometry("400x400+200+20")

button1 = tkinter.Button(win, text="button1", command=button1, width=10, height=10)
button1.pack()

button2 = tkinter.Button(win, text="button2", command=lambda: print("hero is a nice man"))
button2.pack()

button3 = tkinter.Button(win, text="exit", command=win.quit)
button3.pack()

win.mainloop()

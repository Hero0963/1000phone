import tkinter

win = tkinter.Tk()
win.title("HERO")

win.geometry("400x400+200+20")

scale = tkinter.Scale(win, from_=0, to=100, orient=tkinter.HORIZONTAL, tickinterval=10, length=200)
scale.pack()

scale.set(20)

def showNum():
    print(scale.get())


tkinter.Button(win, text="button", command=showNum).pack()

win.mainloop()

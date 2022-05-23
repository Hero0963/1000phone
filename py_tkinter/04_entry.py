import tkinter

win = tkinter.Tk()
win.title("HERO")

win.geometry("400x400+200+20")

e = tkinter.Variable()

# show="*"
entry = tkinter.Entry(win, textvariable=e)
entry.pack()

e.set("hero is a good man")

print(e.get())
print(entry.get())

win.mainloop()

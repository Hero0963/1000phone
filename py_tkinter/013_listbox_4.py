import tkinter

win = tkinter.Tk()
win.title("HERO")

win.geometry("400x400+200+20")

lb = tkinter.Listbox(win, selectmode=tkinter.MULTIPLE)
lb.pack()

for item in ["good", "nice", "handsome", "gg", "qq"]:
    lb.insert(tkinter.END, item)

win.mainloop()

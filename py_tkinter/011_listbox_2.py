import tkinter

win = tkinter.Tk()
win.title("HERO")

win.geometry("400x400+200+20")

lbv = tkinter.StringVar()
lb = tkinter.Listbox(win, selectmode=tkinter.SINGLE, listvariable=lbv)
lb.pack()

for item in ["good", "nice", "handsome", "gg", "qq"]:
    lb.insert(tkinter.END, item)

lb.insert(tkinter.ACTIVE, "cool")

print(lbv.get())

lbv.set(("1", "2", "3"))


def myPrint(event):
    print("*****")
    print(lb.get(lb.curselection()))


lb.bind("<Double-Button-1>", myPrint)

win.mainloop()

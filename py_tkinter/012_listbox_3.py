import tkinter

win = tkinter.Tk()
win.title("HERO")

# win.geometry("400x400+200+20")

# press ctrl shift
lb = tkinter.Listbox(win, selectmode=tkinter.EXTENDED)
lb.pack()

for item in ["good", "nice", "handsome", "vg", "vn",
             "good1", "nice1", "handsome1", "vg1", "vn1",
             "good3", "nice3", "handsome3", "vg3", "vn3"]:
    lb.insert(tkinter.END, item)

sc = tkinter.Scrollbar(win)
sc.pack(side=tkinter.RIGHT, fill=tkinter.Y)
lb.config(yscrollcommand=sc.set)
lb.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
sc["command"] = lb.yview



win.mainloop()

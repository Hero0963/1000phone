import tkinter

win = tkinter.Tk()
win.title("HERO")

win.geometry("400x400+200+20")

lb = tkinter.Listbox(win, selectmode=tkinter.BROWSE)
lb.pack()

for item in ["good", "nice", "handsome", "gg", "qq"]:
    lb.insert(tkinter.END, item)

lb.insert(tkinter.ACTIVE, "cool")
# lb.delete(1,3)

lb.select_set(2, 5)

# lb.select_clear(2, 4)

# print(lb.size())

# print(lb.get(2, 4))

# print(lb.curselection())

print(lb.selection_includes(1))
print(lb.selection_includes(3))

win.mainloop()

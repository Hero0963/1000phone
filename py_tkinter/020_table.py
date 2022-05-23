import tkinter
from tkinter import ttk

win = tkinter.Tk()
win.title("HERO")

win.geometry("400x400+200+20")

tree = ttk.Treeview(win)
tree.pack()

tree["columns"] = ("name", "age", "height", "weight")
tree.column("name", width=100)
tree.column("age", width=100)
tree.column("height", width=100)
tree.column("weight", width=100)

tree.heading("name", text="name")
tree.heading("age", text="age")
tree.heading("height", text="height (cm)")
tree.heading("weight", text="weight (kg)")

tree.insert("", 0, text="line1", values=("hero", "33", "172", "68"))
tree.insert("", 1, text="line2", values=("hero", "34", "173", "69"))
tree.insert("", 2, text="line3", values=("hero", "35", "174", "70"))

win.mainloop()

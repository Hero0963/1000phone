import tkinter
from tkinter import ttk

win = tkinter.Tk()
win.title("HERO")

win.geometry("400x400+200+20")

tree = ttk.Treeview(win)
tree.pack() 

treeF1 = tree.insert("", 0, "Taiwan", text="Taiwan", values=("F1"))
treeF2 = tree.insert("", 1, "USA", text="USA", values=("F2"))
treeF3 = tree.insert("", 2, "UK", text="UK", values=("F3"))

treeF1_1 = tree.insert(treeF1, 0, "Taipei", text="Taipei", values=("F1_1"))
treeF1_2 = tree.insert(treeF1, 1, "Taichung", text="Taichung", values=("F1_2"))
treeF1_3 = tree.insert(treeF1, 2, "Tainan", text="Tainan", values=("F1_3"))

win.mainloop()

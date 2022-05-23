import tkinter
import os

from tree_windows import TreeWindows
from info_windows import InfoWindows

win = tkinter.Tk()
win.title("HERO")

win.geometry("600x400+200+50")

path = r"D:\PythonProject\first\hwTreeDir"
infoWin = InfoWindows(win)
treeWin = TreeWindows(win, path, infoWin)

win.mainloop()

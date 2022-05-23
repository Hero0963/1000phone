import tkinter
from tkinter import ttk
import os


class TreeWindows(tkinter.Frame):
    def __init__(self, master, path, other_win):
        frame = tkinter.Frame(master)
        frame.grid(row=0, column=0)

        self.other_win = other_win

        self.tree = ttk.Treeview(frame)
        self.tree.pack(side=tkinter.LEFT, fill=tkinter.Y)

        tmp_path = self.get_last_path(path)
        root = self.tree.insert("", "end", text=tmp_path, open=True, values=path)
        self.load_tree(root, path)

        # scrollbar
        self.sy = tkinter.Scrollbar(frame)
        self.sy.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        self.sy.config(command=self.tree.yview)
        self.tree.config(yscrollcommand=self.sy.set)

        # bind event
        self.tree.bind("<<TreeviewSelect>>", self.func)

    def func(self, event):
        self.v = event.widget.selection()
        for sv in self.v:
            file = self.tree.item(sv)["text"]
            self.other_win.ev.set(file)
            apath = self.tree.item(sv)["values"][0]
            print(apath)

    def load_tree(self, parent, parent_path):
        for file_name in os.listdir(parent_path):
            abs_path = os.path.join(parent_path, file_name)

            treey = self.tree.insert(parent, "end", text=self.get_last_path(abs_path), values=abs_path)
            if os.path.isdir(abs_path):
                self.load_tree(treey, abs_path)

    def get_last_path(self, path):
        path_list = os.path.split(path)
        return path_list[-1]

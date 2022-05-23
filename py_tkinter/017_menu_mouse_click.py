import tkinter

win = tkinter.Tk()
win.title("HERO")

win.geometry("400x400+200+20")

menubar = tkinter.Menu(win)

menu = tkinter.Menu(menubar, tearoff=False)

for item in ["Python", "C", "C++", "OC", "Swift", "C#", "shell", "Java", "JS", "PHP", "NoseJS", "Exit"]:
    if item == "Exit":
        menu.add_separator()
        menu.add_command(label=item, command=win.quit)
    else:
        menu.add_command(label=item)

menubar.add_cascade(label="PL", menu=menu)


def showMenu(event):
    menubar.post(event.x_root, event.y_root)


win.bind("<Button-3>", showMenu)

win.mainloop()

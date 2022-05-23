import tkinter

win = tkinter.Tk()
win.title("HERO")

win.geometry("400x400+200+20")

menubar = tkinter.Menu(win)
win.config(menu=menubar)


def func():
    print("hero is a good man")


menu1 = tkinter.Menu(menubar, tearoff=False)

for item in ["Python", "C", "C++", "OC", "Swift", "C#", "shell", "Java", "JS", "PHP", "NoseJS", "Exit"]:

    if item == "Exit":
        menu1.add_separator()
        menu1.add_command(label=item, command=win.quit)
    else:
        menu1.add_command(label=item, command=func)

menubar.add_cascade(label="Programming Language", menu=menu1)

menu2 = tkinter.Menu(menubar, tearoff=False)
menu2.add_command(label="red")
menu2.add_command(label="blue")

menubar.add_cascade(label="color", menu=menu2)

win.mainloop()

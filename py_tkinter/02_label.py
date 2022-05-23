import tkinter

win = tkinter.Tk()
win.title("HERO")

win.geometry("400x400+200+20")

label = tkinter.Label(win,
                      text="hero is a good man",
                      bg="pink",
                      fg="red",
                      font=("黑體", 20),
                      width=10,
                      height=4,
                      wraplength=100,
                      justify="left",
                      anchor="center")

label.pack()

win.mainloop()

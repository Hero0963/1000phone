import tkinter

win = tkinter.Tk()
win.title("HERO")

win.geometry("400x400+200+20")

frm = tkinter.Frame(win)
frm.pack()

# left
frm_l = tkinter.Frame(frm)
tkinter.Label(frm_l, text="top left", bg="pink").pack(side=tkinter.TOP)
tkinter.Label(frm_l, text="bottom left", bg="blue").pack(side=tkinter.TOP)
frm_l.pack(side=tkinter.LEFT)

# right
frm_r = tkinter.Frame(frm)
tkinter.Label(frm_r, text="top right", bg="red").pack(side=tkinter.TOP)
tkinter.Label(frm_r, text="bottom right", bg="yellow").pack(side=tkinter.TOP)
frm_r.pack(side=tkinter.RIGHT)

win.mainloop()

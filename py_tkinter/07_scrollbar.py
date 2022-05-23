import tkinter

win = tkinter.Tk()
win.title("HERO")


scroll = tkinter.Scrollbar()
text = tkinter.Text(win, width=50, height=8)

scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)
text.pack(side=tkinter.LEFT, fill=tkinter.Y)

scroll.config(command=text.yview)
text.config(yscrollcommand=scroll.set)

str1 = """In faith I do not love thee with mine eyes,
For they in thee a thousand errors note;
But `tis my heart that loves what they despise,
Who in despite of view is pleased to dote.
Nor are mine ears with thy tongue`s tune delighted;
Nor tender feeling to base touches prone,
Nor taste, nor smell, desire to be invited
To any sensual feast with thee alone.
But my five wits, nor my five senses can
Dissuade one foolish heart from serving thee,
Who leaves unswayed the likeness of a man,
Thy proud heart`s slave and vassal wretch to be.
Only my plague thus far I count my gain,
That she that makes me sin awards me pain.
"""

text.insert(tkinter.INSERT, str1)

win.mainloop()

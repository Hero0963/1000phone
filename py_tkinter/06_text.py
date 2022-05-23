import tkinter

win = tkinter.Tk()
win.title("HERO")

win.geometry("400x400+200+20")

text = tkinter.Text(win, width=30, height=4)
text.pack()

# str = "Let me not to the marriage of true minds \n " \
#       "Admit impediments. Love is not love \n " \
#       "Which alters when it " \
#       "alteration finds, \n " \
#       "Or bends with the remover to remove: \n " \
#       "O, no! it is an ever-fix`ed mark, \n " \
#       "That looks on tempests and is never shaken; \n" \
#       "It is the star to every wand'ring bark, \n" \
#       "Whose worth's unknown, although his heighth be taken. \n" \
#       "Love's not Time's fool, though rosy lips and cheeks \n" \
#       "Within his bending sickle's compass come; \n" \
#       "Love alters not with his brief hours and weeks, \n" \
#       "But bears it out even to the edge of doom: \n" \
#       "If this be error and upon me proved, \n" \
#       "I never writ, nor no man ever loved. \n"

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

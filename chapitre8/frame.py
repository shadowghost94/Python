from tkinter import *

fen= Tk()
Frame1= Frame(fen, borderwidth=30, relief=RAISED, bg="yellow")
Frame1.pack(side=LEFT, padx=30, pady=30)

Label(Frame1, text="Eh oui, c'est bien un Frame").pack(padx=10, pady=10)

fen.mainloop()

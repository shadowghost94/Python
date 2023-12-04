#Recevoir une entrée
from tkinter import *

fen= Tk()
can= Canvas(fen, width=400, height=400, bg='white')
can.pack()

#value=StringVar()
#value.set("texte par défaut")
entree= Entry(fen, textvariable="string", width=50)
entree.pack()
#entree.grid(row=0, sticky=E)

fen.mainloop()

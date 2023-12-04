from tkinter import *
from math import *

#definition de l'action à effectuer si l'utilisateur actionne
#la touche "entrer" alors qu'il edite le champ d'entré

def evaluer(event):
    chaine.configure(text= "Résultat= "+ str( eval(entree.get()) ))

#---------Programme principal-------------------------------
fen= Tk()
entree=Entry(fen)
entree.bind("<Return>", evaluer)
chaine= Label(fen)
entree.pack()
#chaine.pack()

fen.mainloop()

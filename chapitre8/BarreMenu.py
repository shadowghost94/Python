from tkinter import *
from tkinter.messagebox import *

fen= Tk()

def alert(receveur):
    showinfo("Alerte", "receveur")

menubar= Menu(fen)

menu1= Menu(menubar, tearoff=0)
menu1.add_command(label="Créer", command=alert("Céer !") )
menu1.add_command(label="Editer", command=alert("Editer !") )
menu1.add_separator()
menu1.add_command(label="Quitter", command=fen.quit)
menubar.add_cascade(label="Fichier", menu=menu1)

menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="Couper", command=alert("Couper !") )
menu2.add_command(label="Copier", command=alert("Copier") )
menu2.add_command(label="Coller", command=alert("Coller") )
menubar.add_cascade(label="Editer", menu=menu2 )

menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="A propos", command=alert)
menubar.add_cascade(label="Aide", menu=menu3)


#fen.config(menu=menubar)
fen.mainloop()

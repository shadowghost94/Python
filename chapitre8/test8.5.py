from tkinter import *
from random import randrange

def drawline():
    "Tracé d'une ligne dans le canevas"
    global x1, y1, x2, y2, coul
    can1.create_polygon(x1, y1, x2, y2, width=2, fill=coul)

    #modification des coordonnées pour la ligne suivante
    y2,y1= y2+10, y1-10

def changecolor():
        "changement aléatoire de la couleur du tracé"
        global coul
        pal=['cyan', 'maroon', 'green']
        c=randrange(8)
        coul=pal[c]

x1,y1, x2, y2=10, 190, 190, 10
coul= 'dark green'

#création du widget principal
fen1= Tk()

#création des widgets esclaves
can1= Canvas(fen1, bg='dark grey', height=500, width=500)
can1.pack()

bou1= Button(fen1, text='Quitter', command=fen1.quit)
bou1.pack(side=BOTTOM)

bou2= Button(fen1, text='Tracer une ligne', command=drawline)
bou2.pack()

bou3= Button(fen1, text='Autre couleur', command=changecolor)
bou3.pack()

fen1.mainloop()  #demarrage du réceptionnaire d'événements
fen1.destroy()  #destruction (fermetture) de la fenêtre

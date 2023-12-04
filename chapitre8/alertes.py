#Liste des alertes possible
#showinfo()
#showwarning()
#showerror()
#askquestion()
#askokcancel()
#askyesno()
#askretrycancel()

from tkinter import *
from tkinter.messagebox import *

fen= Tk()
def callback():
    if askyesno('Titre 1', 'Êtes-vous sûr de vouloir faire ça ?'):
        showwarning('Titre 2', 'Tant pis ...')
    else:
        showinfo('Titre 3', 'Vous avez peur !')
        showerror('Titre 4', 'Aha')

Button(text="Appuyer", command=callback).pack()

fen.mainloop()

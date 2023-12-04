from tkinter import *

#création du widget
fen=Tk()

p=PanedWindow(fen, orient=VERTICAL)
p.pack(side=TOP, expand=Y, fill=BOTH, pady=2, padx=2)
p.add( Label(p, text='vert', background='green', anchor=CENTER) )
p.add( Label(p, text='Jaune', background='yellow', anchor=CENTER) )
p.add( Label(p, text='Rouge', background='red', anchor=CENTER) )
#p.pack()

fen.mainloop()

from tkinter import *
import time
fen = Tk()
can=Canvas(fen,width=500,height=500,background='white')
can.pack()
balle=can.create_oval(10,250,30,270,fill="red")
while True:
    can.move(balle,1,0)
    fen.update_idletasks()
    fen.update()
    time.sleep(0.01)

fen.mainloop()

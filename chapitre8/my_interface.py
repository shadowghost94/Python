from tkinter import *

fen= Tk()
can= Canvas(fen, width=500, height=500, bg='white')
can.pack(side=TOP, padx=5, pady=5)
can.create_line(50, 50, 0, 50, fill='blue')

fen.mainloop()

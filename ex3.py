tableau=[32, 5, 12, 8, 3, 75, 2, 15]

i=1
temoin=tableau[0]
while i<( len(tableau) -1 ):
    if( tableau[i]>temoin ):
        temoin=tableau[i]
    i=i+1
print(temoin)

""" je créé un plateau d'échiquier en utilisant les notions de dictionnaire"""

echiquier=dict()
#echiquier={}

echiquier['a', 1]= "tour blanche gauche"
echiquier['h', 1]= "tour blanche droite"
echiquier['b', 1]= "chevalier blanc gauche"
echiquier['g', 1]= "chevalier blanc droite"
echiquier['c', 1]= "fou blanc gauche"
echiquier['f', 1]= "fou blanc droite"
echiquier['d', 1]= "Reine blanche"
echiquier['e', 1]= "Roi blanc"

#placard={"chemise":6, "pantalon":6, "tee-shirt":6}

for indice,valeur in echiquier.items():
    print()

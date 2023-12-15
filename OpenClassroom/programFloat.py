"""Ce programme test une fonction qui permet de diviser un flottant en deux parties: partie décimale et partie flottante
        On récupère la partie décimale et la partie entière de façon indépendante
        puis on le remets ensemble en remplaçant le point d'origine par une virgule
        on limitera la partie flottante à trois chiffres après la virgule
"""

def fonc(flottant):

    #première étape, on s'assure qu'on reçoit éffectivement in flottant
    if type(flottant) is not float:
        raise TypeError("le paramètre attendu doit être un flottant")

    #deuxième étape, on convertit le flottant en string
    flottant=str(flottant)

    #troisième étape on subdivise notre flottant en deux parties grâce à la fonction split()
    partie_entiere, partie_flottant= flottant.split(".")

    #on retourne enfin les deux parties de manière à tronquer
    return ",".join([partie_entiere, partie_flottant[:3] ])

print(fonc(3.999999999999))
print(fonc(4.888888888888))
print(fonc(5.777777777777))

#je crée une fonction dont on ne connait pas à l'avance le nombre de paramètre
def fonc_unknow(*parametres):
    print(type(parametres))
    print("J'ai reçu {}.".format(parametres))

fonc_unknow("hello world", 2, "Winterfell")

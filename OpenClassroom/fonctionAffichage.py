"""
    On crée une fonction similaire à la foncion print()
"""

def affichage(*values, sep=' ', end='\n'):
    i=0
    phrase=str()

    while i<len(values):
        phrase+=values[i]
        phrase+=sep
        i=i+1

    print(phrase)

affichage("Bonjour","la","familia","je","suis","enchanté","de","voir","que","ma","fonction","fonctionne","correctement")

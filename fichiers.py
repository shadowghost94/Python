import os
objet_fichier=open("my_txt.txt","a")
objet_fichier.write("Eh oui je sui bien celui que tu pense !\n")
objet_fichier.write("Je suis le magicien de l'enfer !\n")

lire= objet_fichier.read()
print(lire)
objet_fichier.close()

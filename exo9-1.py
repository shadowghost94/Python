name_file= input("veuillez entrer le nom de votre fichier: ")

nbr= input("1- Ajouter de nouvelles lignes de code \n 2- Afficher le contenu du fichier \n ...: ")
nbr=int(nbr)
if(nbr==1):
    texte="..."
    while texte!="":
        texte= input("Veuillez entrer à chaque fois le texte à ajouter dans le fichier.  Apuyez sur Entrer pour annuler: ")
        objet0= open(name_file, "a")
        objet0.write(texte+"\n")
        objet0.close()

elif (nbr==2):
    objet1= open(name_file, "r")
    #while 1:
        #objet2= objet1.readline()
        #print(objet2)
        #objet1.close()
    objet2= objet1.readlines()
    print (objet2)

else:
    print("Vous avez entré une mauvaise valeur! ")

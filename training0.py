#Ecrire un programme qui prend une liste de chaines de caractères en
#listes de chaine et renvoie la plus longues chaine de caractère de la liste

my_list= [ "je sui là", "Je suis un con", "priez à l'heure les frères", "la route du dévéloppement", "passe par le dévéloppement de la route"]

indice=[]
i=0
#la boucle suivante détermine pour chaque indice de liste le nombre de caractère
while (i<len(my_list)):
    indice.append( len( my_list[i] ) )
    i=i+1

temoins=indice[0]
i=1
while (i<len(my_list)):
    if( indice[0]<indice[i] ):
        temoins=i
    i=i+1

print("La plus grande chaine est: {}".format(my_list[temoins]) )

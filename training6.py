#Ecrire un programme qui prend deux listes d'entiers
#en entré et renvoie  une nouvelle liste  contenant
#les éléments communs aux deux listes.


list1=[1,2,3,4,5,6,7,8,9]
list2=[9,7,11,12,16,1,5]
def CommunTwins(firstList, secondList):
    nouvelle_list=[]
    i=0
    while(i< len(firstList)):
        j=0
        while(j<len(secondList)):
            if( firstList[i]==secondList[j]):
                nouvelle_list.append(firstList[i])
            j=j+1
        i=i+1
    return nouvelle_list;
print( CommunTwins(list1, list2) )

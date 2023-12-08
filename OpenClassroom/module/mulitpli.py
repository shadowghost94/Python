def multiplicateur(nombre):
    i=0
    while i< 10:
        valeur=nombre*i
        print( nombre,"*",i,"=",valeur )
        i+=1
if __name__=="__main__":
    multiplicateur(5)

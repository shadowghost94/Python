#!/usr/bin/python3
# -*- coding: utf-8 -*-

print("Ce programme vous permet de savoir si une année entré est bissextile ou pas .")
valeur= input("veuillez entrer une année: ")
valeur= int(valeur)

if valeur%4 == 0:
    if( valeur%100 == 0):
        if( valeur % 400 == 0):
            print("L'année que vous avez entré au clavier est bissextile.")
        else:
            print("L'année que vous avez entré au clavier n'est pas bissextile.")
    else:
        print("L'année que vous avez entré au clavier n'est pas bissextile.")
else:
    print("Ce n'est pas une année bissextile.")

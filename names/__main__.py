#!/usr/bin/python3

# from baza import *


import baza

autozapis = "N"
baza_imion = []
opcja = ""

while opcja != "0":
    opcja = baza.menu(autozapis)
    if opcja == "1":
        baza_imion = baza.dodaj(baza_imion, autozapis)
    elif opcja == "2":
        baza_imion = baza.usun(baza_imion, autozapis)
    elif opcja == "3":
        baza.szukaj(baza_imion)
    elif opcja == "4":
        baza.policz(baza_imion)
    elif opcja == "5":
        baza.pokaz(baza_imion)
    elif opcja == "6":
        baza.zapisz(baza_imion)
    elif opcja == "7":
        baza_imion = baza.wczytaj()
    elif opcja == "8":
        if autozapis == "T":
            autozapis = "N"
        elif autozapis == "N":
            autozapis = "T"
    elif opcja == "9":
        baza_imion = baza.wyczysc()
    elif opcja != "0":
        baza.nieznane_polecenie()

print("Koniec pracy")
exit(0)

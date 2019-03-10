import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def any_key():
    print()
    temp = input("Naciśnij [ENTER]")


def menu(autozapis):
    cls()
    print(" M E N U")
    print("=" * 9)
    print("1..dodawanie imienia")
    print("2..usuwanie imienia")
    print("3..szukanie imienia")
    print("4..sprawdzenie ilości imion")
    print("5..lista imion w bazie")
    print()
    print("6..zapis bazy na dysk")
    print("7..odczyt bazy z dysku")
    print("8..zapis po kazdej operacji:", autozapis)
    print()
    print("9..wyczyść bazę")
    print()
    print("0..koniec")
    print()
    wybor = input("Podaj swój wybór: ")
    return wybor


def dodaj(baza_imion, autozapis):
    print("1..dodawanie imienia")
    print()
    imie = input("Podaj imie: ")
    if imie == "":
        print("Nie podałeś imienia. Nic nie dodałem :(")
        return
    baza_imion.append(imie)
    print("Dodałem imię: {}".format(imie))
    if autozapis == "T":
        zapisz(baza_imion)
    any_key()
    return baza_imion


def usun(baza_imion, autozapis):
    print("2..usuwanie imienia")
    print()
    imie = input("Podaj imie: ")
    if imie == "":
        print("Nie podałeś imienia. Nic nie usunąłem :(")
        any_key()
        return
    elif imie not in baza_imion:
        print("Brak imienia w bazie danych.")
        any_key()
        return
    baza_imion.remove(imie)
    print("Usunąłem imię: {}".format(imie))
    if autozapis == "T":
        zapisz(baza_imion)
    any_key()
    return baza_imion


def szukaj(baza_imion):
    print("3..szukanie imienia")
    print()
    imie = input("Podaj imie: ")
    if imie == "":
        print("Nie podałeś imienia. Niczego nie znalazłem :(")
        any_key()
        return
    wynik = baza_imion.count(imie)
    if wynik > 0:
        print("Ilosc imion w bazie: {}".format(wynik))
    else:
        print("Nie ma takiego imienia.")
    any_key()


def policz(baza_imion):
    print("4..sprawdzenie ilości imion")
    print()
    print("Ilosc imion w bazie: {}".format(len(baza_imion)))
    print()
    any_key()


def pokaz(baza_imion):
    print("5..lista imion w bazie")
    print()
    print(baza_imion)
    print()
    any_key()


def zapisz(baza_imion):
    with open("baza.txt", "w") as plik:
        for imie in baza_imion:
            plik.write(imie + "\n")
    print("Baza zapisana.")
    any_key()


def wczytaj():
    baza_imion = []
    with open("baza.txt", "r") as plik:
        baza_imion = plik.read().split()
    print("Baza wczytana")
    any_key()
    return baza_imion


def wyczysc():
    odpowiedz = input("Czy na pewno? (t/n)")
    if odpowiedz == "t":
        print("Baza wyczyszczona!")
        any_key()
    return []


def nieznane_polecenie():
    print("Nieznane polecenie")
    any_key()

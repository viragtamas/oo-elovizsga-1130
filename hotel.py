#Hozz létre egy Szoba absztrakt osztályt, amely alapvető attribútumokat definiál (ár, szobaszám). (5 pont)

from abc import ABC, abstractmethod
from datetime import datetime

class Szoba(ABC):
    def __init__(self, szobaszam, ar):
        self.ar = ar
        self.szobaszam = szobaszam

#Hozz létre az Szoba osztályból EgyagyasSzoba és KetagyasSzoba származtatott osztályokat, amelyek különböző attributumai vannak, és az áruk is különböző.(5 pont)

class EgyagyasSzoba(Szoba):
    def __int__(self):
        self.ferohely = 1
        self.ar = 20000


class KetagyasSzoba(Szoba):
    def __init__(self):
        self.ferohely = 2
        self.ar = 30000


# Hozz létre egy Foglalás osztályt, amelybe a Szálloda szobáinak foglalását tároljuk (elég itt, ha egy foglalás csak egy napra szól)

class Foglalas:
    def __init__(self, szoba, datum):
        self.szoba = szoba
        self.datum = datum

    def __str__(self):
        return f"A foglalt szoba száma {self.szoba} a {self.datum} napra."


#Hozz létre egy Szalloda osztályt, ami ezekből a Szobákból áll, és van saját attributuma is (név pl.)

class Szalloda:
    def __init__(self):
        self.szobak = []
        self.foglalasok = []
        self.nev = "Virág Tamás objektumorientált szállodája"

    def uj_szoba(self, szoba: Szoba):
        self.szobak.append(szoba)

    def uj_foglalas(self, foglal: Foglalas):
        self.foglalasok.append(foglal)

    def foglalas_listazas(self):
        print("A következő foglalások vannak a rendszerben:")
        for foglalas in self.foglalasok:
            print(foglalas)

    def szabadszobak(self, szemelyek, datum):
        for szoba in self.szobak:
            for van in self.foglalasok:
                if szoba.szobaszam != van.szoba and datum != van.datum:
                    self.uj_foglalas(Foglalas(szoba.szobaszam, datum))
                    print (f"lefoglalva a {szoba.szobaszam} számú szoba {datum} napra")
                    return
                else:
                    print (f"A {szoba.szobaszam} számú szoba nem szabad")


    def feltolt(self):
        self.uj_szoba(EgyagyasSzoba(101, 35000))
        self.uj_szoba(EgyagyasSzoba(102, 35000))
        self.uj_szoba(EgyagyasSzoba(103, 36000))
        self.uj_foglalas(Foglalas(101, 20240101))
        self.uj_foglalas(Foglalas(101, 20240102))
        self.uj_foglalas(Foglalas(102, 20240103))
        self.uj_foglalas(Foglalas(103, 20240105))
        self.uj_foglalas(Foglalas(103, 20240106))
        #print("Sikeres feltöltés")





#Készíts egy egyszerű felhasználói interfészt, ahol a felhasználó kiválaszthatja a kívánt műveletet (pl. foglalás, lemondás, listázás). (20 pont)

def foglalaskezeles(szallodam: Szalloda):
#Töltsd fel az futtatás után a rendszert 1 szállodával, 3 szobával és 5 foglalással, mielőtt a felhasználói adatbekérés megjelenik.
    szallodam.feltolt()

    while True:
        print("Adja meg, hogy mit szeretne tenni:")
        print("1. Foglalás")
        print("2. Lemondás")
        print("3. Listázás")
        print("4. Kilépés")
        muvelet = input("Adja meg a kívánt művelet sorszámát: ")
        if muvelet == "1":
            szemelyek = input("Hány főre kíván szobát foglalni? 1 vagy 2?")
            kezdonap =input("Mikor érkezik: ÉÉÉÉHHNN formában adja meg?")
            szalloda.szabadszobak(szemelyek, kezdonap)
        elif muvelet == "2":
            pass
        elif muvelet == "3":
            szalloda.foglalas_listazas()
        elif muvelet == "4":
            break
        else:
            print("Nem megfelelő menüpont")


szalloda = Szalloda()
foglalaskezeles(szalloda)
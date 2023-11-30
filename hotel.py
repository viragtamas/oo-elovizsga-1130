#Hozz létre egy Szoba absztrakt osztályt, amely alapvető attribútumokat definiál (ár, szobaszám). (5 pont)

from abc import ABC, abstractmethod

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

#Hozz létre egy Szalloda osztályt, ami ezekből a Szobákból áll, és van saját attributuma is (név pl.)

class Szalloda:
    def __int__(self):
        self.szobak = []
        self.nev = "Virág Tamás objektumorientált szállodája"


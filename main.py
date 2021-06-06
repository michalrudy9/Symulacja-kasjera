import random
from datetime import datetime
import time
from tkinter import Tk, Canvas

from TowarNaSztuki import TowarNaSztuki
from TowarNaWage import TowarNaWage
from grafika import Grafika
from wyjatki import TowarNieZwazonyWyjatek, ZaDuzaWartoscPolaTekstowegoWyjatek

nazwyProduktow = ['Pstrąg', 'Kakao', 'Mango', 'Gruszka', 'Kapusta', 'Kiwi', 'Groch', 'Granat', 'Tuńczyk','Banan', 'Ziemniak', 'Cukinia', 'Pomidor',  'Jabłko', 'Cytryna', 'Czekolada', 'Marchewka', 'Arbuz', 'Chleb', 'Makaron', 'Dorsz', 'Ananas']
listaTowarow = []
licznikTowarow = 0
czasStartu = time.perf_counter()
randRozmiar = 0
zwazonyTowar = False
global aktualnyIndexTowaru
global grafika
global aktualnyTypTowaru
global aktualnyTowar
przegrana = False
koniec = False


def start():
   """Gówna funkcja programu, odpowida za mechanikę programu"""
   global licznikTowarow, czasStartu, randRozmiar, listaTowarow, aktualnyIndexTowaru, przegrana, koniec

   przegrana = False
   koniec = False
   licznikTowarow = 0
   czasStartu = time.perf_counter()
   randRozmiar = random.randint(10, 20)
   listaTowarow = wymieszajTowary([TowarNaSztuki(nazwyProduktow) if i < int(randRozmiar / 2) else TowarNaWage(nazwyProduktow) for i in range(randRozmiar)])
   aktualnyIndexTowaru = 0
   ustawInfroAktualnegoProduktu(aktualnyIndexTowaru)
   pokazTowarNaWage(aktualnyTowar) if aktualnyTypTowaru == TowarNaWage else pokazTowarNaSztuki(aktualnyTowar)


def main():
   global grafika

   if __name__ == "__main__":
      root = Tk()
      root.title('Symulacja kasjera')
      root.geometry('1000x500')
      root.resizable(width=False, height=False)

      linia = Canvas(root, height=500, width=1000)
      linia.create_line(500, 0, 500, 500)
      linia.grid()

      grafika = Grafika(root, start, kliknietyTowar, zwaz)

      root.mainloop()


def wymieszajTowary(lista):
   """Funkcja odpowiedzialna za mieszanie kolejności towarów z listy"""
   random.shuffle(lista)
   return lista


def ustawInfroAktualnegoProduktu(index):
   """Funkcja ustawia aktualny towar oraz jego dane"""
   global aktualnyTypTowaru, aktualnyTowar

   aktualnyTowar = listaTowarow[index]
   aktualnyTowar.czasPojawieniaSieWOknie = datetime.now()
   aktualnyTypTowaru = type(aktualnyTowar)


def pokazTowarNaWage(towar: TowarNaWage):
   """Funkcja wyświetlająca kolejny towar (towar na wagę) wykonująca się w obiekcie 'grafika'"""
   grafika.pokazTowar(towar.nazwaTowaru + ' ?kg')


def pokazTowarNaSztuki(towar: TowarNaSztuki):
   """Funkcja wyświetlająca kolejny towar (towar na sztuki) wykonująca się w obiekcie 'grafika'"""
   grafika.pokazTowar(towar.nazwaTowaru + ' x' + str(towar.ilosc))


def kliknietyTowar(ilosc):
   """Funkcja wywoływana po naciśniecu przycisku z towarem"""
   global zwazonyTowar, licznikTowarow, przegrana

   try:
      if zwazonyTowar:
         zwazonyTowar = False
         raise TowarNieZwazonyWyjatek()
      else:
         if aktualnyTypTowaru == TowarNaWage:
            if czyTowarNaWageZwazony(aktualnyTowar):
               licznikTowarow += 1
               aktualnyTowar.czasSkasowania = datetime.now()
               grafika.wyczyscPole()
               pokazNastepnyTowar()
            else:
               zwazonyTowar = True
         else:
            kliknietyTowarTowarNaSztuki(aktualnyTowar, ilosc)
   except TowarNieZwazonyWyjatek:
      przegrana = True
      grafika.pokazPrzegralesInformacje()


def czyTowarNaWageZwazony(towar: TowarNaWage):
   """Funkcja sprawdza czy towar na wagę został zważony"""
   return True if towar.czyZwazony else False


def zwaz():
   """Funkcja odpowiedzialna za akcjcę ważenie towaru oraz wywołanie kolejnego towaru"""
   global zwazonyTowar, przegrana, zwazonyTowar

   try:
      if aktualnyTypTowaru == TowarNaWage:
         if zwazonyTowar:
            zwazonyTowar = False
            aktualnyTowar.czyZwazony = True
            grafika.pokazTowar(aktualnyTowar.nazwaTowaru + ' ' + str(aktualnyTowar.waga) + ' kg')
      else:
         raise TowarNieZwazonyWyjatek

   except:
      przegrana = True
      grafika.pokazPrzegralesInformacje()


def pokazNastepnyTowar():
   """Funkcja wykonuje wypisywanie na ekran kolejnego towaru"""
   global licznikTowarow, aktualnyIndexTowaru, listaTowarow

   aktualnyIndexTowaru += 1
   if aktualnyIndexTowaru != len(listaTowarow):
      ustawInfroAktualnegoProduktu(aktualnyIndexTowaru)
      pokazTowarNaWage(aktualnyTowar) if type(aktualnyTowar) == TowarNaWage else pokazTowarNaSztuki(aktualnyTowar)
   else:
      koniecFunkcja()


def inkrementacjaLicznikTowarowTowarNaSztuki(towar: TowarNaSztuki):
   """Funkcja inkrementuje licznik towarów o ilość aktualnego towaru"""
   global licznikTowarow
   licznikTowarow += towar.ilosc


def kliknietyTowarTowarNaSztuki(towar: TowarNaSztuki, iloscZPola):
   """Funkcja odpowiedzialna za obsługę przycisku z towarem"""
   global przegrana

   try:
      if towar.ilosc - iloscZPola < 0:
         raise ZaDuzaWartoscPolaTekstowegoWyjatek()
      else:
         if towar.ilosc - iloscZPola == 0:
            inkrementacjaLicznikTowarowTowarNaSztuki(aktualnyTowar)
            grafika.wyczyscPole()
            pokazNastepnyTowar()
         else:
            towar.ilosc -= iloscZPola
            grafika.wyczyscPole()
            grafika.pokazTowar(towar.nazwaTowaru + ' x' + str(towar.ilosc))
   except ZaDuzaWartoscPolaTekstowegoWyjatek:
      przegrana = True
      grafika.pokazPrzegralesInformacje()


def koniecFunkcja():
   """Funkcja wyświetla na ekranie końcowy wynik programu oraz czas kasowania"""
   global koniec, czasStartu, licznikTowarow

   koniec = True
   czas = round(time.perf_counter() - czasStartu)
   srednia = czas/20
   grafika.pokazPrzegralesInformacje(srednia)

main()
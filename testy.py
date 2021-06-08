import time
import unittest
from tkinter import Tk

import main
from grafika import Grafika


class Test(unittest.TestCase):
    def test1(self):
        root = Tk()
        root.title('Symulacja kasjera')
        root.geometry('1000x500')
        root.resizable(width=False, height=False)
        grafika = Grafika(root, main.start, main.kliknietyTowar, main.zwaz)
        root.update()

        main.grafika = grafika
        main.start()
        main.grafika.ukryjNastepnyKlientIRozpocznij()
        main.listaTowarow[1] = main.TowarNaSztuki(main.nazwyProduktow)
        main.pokazNastepnyTowar()
        root.update()
        aktualnyTowar: main.TowarNaSztuki = main.aktualnyTowar

        for i in range(aktualnyTowar.ilosc):
            main.kliknietyTowar(1)
            root.update()

        self.assertEqual(main.aktualnyIndexTowaru, 2)


    def test2(self):
        root = Tk()
        root.title('Symulacja kasjera')
        root.geometry('1000x500')
        root.resizable(width=False, height=False)
        grafika = Grafika(root, main.start, main.kliknietyTowar, main.zwaz)
        root.update()

        main.grafika = grafika
        main.start()
        main.grafika.ukryjNastepnyKlientIRozpocznij()
        main.listaTowarow[1] = main.TowarNaSztuki(main.nazwyProduktow)
        main.pokazNastepnyTowar()
        root.update()
        aktualnyTowar: main.TowarNaSztuki = main.aktualnyTowar

        main.kliknietyTowar(aktualnyTowar.ilosc)
        root.update()

        self.assertEqual(main.aktualnyIndexTowaru, 2)
        self.assertEqual(int(main.grafika.poleTekstowe.get()), 1)


    def test3(self):
        root = Tk()
        root.title('Symulacja kasjera')
        root.geometry('1000x500')
        root.resizable(width=False, height=False)
        grafika = Grafika(root, main.start, main.kliknietyTowar, main.zwaz)
        root.update()

        main.grafika = grafika
        main.start()
        main.grafika.ukryjNastepnyKlientIRozpocznij()
        main.listaTowarow[1] = main.TowarNaSztuki(main.nazwyProduktow)
        main.pokazNastepnyTowar()
        root.update()
        aktualnyTowar: main.TowarNaSztuki = main.aktualnyTowar

        main.kliknietyTowarTowarNaSztuki(main.aktualnyTowar, aktualnyTowar.ilosc+1)
        self.assertEqual(main.przegrana, True)


    def test4(self):
        root = Tk()
        root.title('Symulacja kasjera')
        root.geometry('1000x500')
        root.resizable(width=False, height=False)
        grafika = Grafika(root, main.start, main.kliknietyTowar, main.zwaz)
        root.update()

        main.grafika = grafika
        main.start()
        main.grafika.ukryjNastepnyKlientIRozpocznij()
        main.listaTowarow[1] = main.TowarNaSztuki(main.nazwyProduktow)
        main.pokazNastepnyTowar()
        root.update()

        main.zwaz()

        self.assertEqual(main.przegrana, True)


    def test5(self):
        root = Tk()
        root.title('Symulacja kasjera')
        root.geometry('1000x500')
        root.resizable(width=False, height=False)
        grafika = Grafika(root, main.start, main.kliknietyTowar, main.zwaz)
        root.update()

        main.grafika = grafika
        main.start()
        main.grafika.ukryjNastepnyKlientIRozpocznij()
        main.listaTowarow[1] = main.TowarNaWage(main.nazwyProduktow)
        main.pokazNastepnyTowar()
        root.update()

        main.kliknietyTowar(1)
        main.kliknietyTowar(1)

        root.update()

        self.assertEqual(main.przegrana, True)


    def test6(self):
        root = Tk()
        root.title('Symulacja kasjera')
        root.geometry('1000x500')
        root.resizable(width=False, height=False)
        grafika = Grafika(root, main.start, main.kliknietyTowar, main.zwaz)
        root.update()

        main.grafika = grafika
        main.start()
        main.grafika.ukryjNastepnyKlientIRozpocznij()
        root.update()

        for i in range(len(main.listaTowarow)):
            if main.aktualnyTypTowaru == main.TowarNaWage:
                main.kliknietyTowar(1)
                main.zwaz()
                root.update()

                main.kliknietyTowar(1)
                root.update()

            else:
                aktualnyTowar: main.TowarNaSztuki = main.aktualnyTowar
                main.kliknietyTowar(aktualnyTowar.ilosc)
                root.update()

            root.update()

            self.assertEqual(main.koniec, True)

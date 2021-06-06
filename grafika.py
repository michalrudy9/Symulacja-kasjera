import random
from tkinter import Tk, Frame, Button, Label, Entry, END, DISABLED, NORMAL, BOTH, Canvas


class Grafika:
    def __init__(self, root, startFunkcja, kliknietyTowarFunkcja, zwazFunkcja):
        self.root = root
        self.startFunkcja = startFunkcja
        self.kliknietyTowarFunkcja = kliknietyTowarFunkcja
        self.zwazFunkcja = zwazFunkcja

        self.ramkaStracone = Frame(master=self.root)
        self.ramkaKoncowe = Frame(master=self.root)

        self.linia = Canvas(root, height=500, width=1000)
        self.linia.create_line(500, 0, 500, 500)
        self.linia.grid()

        self.sprobujPonownie = Button(master=self.ramkaStracone, text='Sprobój ponownie', command=lambda: self.sprobujPonownieFunkcja())
        self.sprobujPonownie.place(x=400, y=400, height=60, width=200)

        self.przegrales = Label(master=self.ramkaStracone, text='Przegrałeś!')
        self.przegrales.place(x=450, y=200, height=60, width=100)

        self.info = Label(master=self.ramkaStracone, text='Wartość pola tekstowego po prawej stronie przewyższa liczebność towaru!')
        self.info.place(x=250, y=250, height=60, width=500)

        self.sprobujPonownieKoniec = Button(master=self.ramkaKoncowe, text='Sprobój ponownie', command=lambda: self.sprobujPonownieKoniecFunkcja())
        self.sprobujPonownieKoniec.place(x=400, y=400, height=60, width=200)

        self.koniec = Label(master=self.ramkaKoncowe, text='Wygrałeś!')
        self.koniec.place(x=450, y=200, height=60, width=100)

        self.czas = Label(master=self.ramkaKoncowe)
        self.czas.place(x=0, y=250, height=60, width=1000)

        #klaw. numeryczna
        listOfLabelButtons = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        numericButtons = []
        self.finallyCreatedButton = []

        for label in range(10):
            numericButtons.append(listOfLabelButtons[label])

        positionX = 660
        positionY = 80
        for button in range(len(numericButtons) - 1):
            if button % 3 == 0:
                positionY += 60
                positionX = 600
            self.finallyCreatedButton.append(Button(self.root, text=numericButtons[button]))
            self.finallyCreatedButton[button].bind('<Button-1>', lambda event, b=button: self.dodajLiczbeDoPola(listOfLabelButtons[b]))
            self.finallyCreatedButton[button].place(x=positionX, y=positionY, height=60, width=60)
            positionX += 60
        positionX = 600
        positionY += 60
        self.finallyCreatedButton.append(Button(self.root, text=numericButtons[len(numericButtons) - 1]))
        self.finallyCreatedButton[len(numericButtons) - 1].bind('<Button-1>', lambda event, b=button: self.dodajLiczbeDoPola(listOfLabelButtons[len(numericButtons) - 1]))
        self.finallyCreatedButton[len(numericButtons) - 1].place(x=positionX, y=positionY, height=60, width=180)

        self.wyczysc = Button(root, text='Wyczysc', command=lambda: self.wyczyscPole())
        self.wyczysc.place(x=780, y=140, height=60, width=120)

        self.backspace = Button(root, text='Backspace', command=lambda: self.usonOstatniZnak())
        self.backspace.place(x=780, y=200, height=60, width=120)

        self.zwaz = Button(root, text='Zważ', command=lambda: self.zwazFunkcja())
        self.zwaz.place(x=780, y=260, height=120, width=120)

        self.poleTekstowe = Entry(self.root)
        self.poleTekstowe.place(x=600, y=50, height=50, width=300)
        self.poleTekstowe.insert(END, '1')
        self.poleTekstowe.configure(state=DISABLED)

        self.nastepnyKlient = Button(root, text='Następny klient', command=lambda: self.ukryjNastepnyKlientIRozpocznij())
        self.nastepnyKlient.place(x=170, y=210, height=60, width=150)

        self.przyciskNaTowar = Button(root, command=lambda: self.kliknietyTowarFunkcja(int(self.poleTekstowe.get())))

        self.wyczyszczonePoleTekstowe = True



    def dodajLiczbeDoPola(self, liczba):
        """Metoda dodaje do pola tekstowego liczbe"""
        self.poleTekstowe.configure(state = NORMAL)
        if self.wyczyszczonePoleTekstowe:
            self.poleTekstowe.delete(0, END)
            self.poleTekstowe.insert(0, liczba)
            self.wyczyszczonePoleTekstowe = False
        else:
            aktualnaLiczbaWPolu = self.poleTekstowe.get()
            self.poleTekstowe.delete(0, END)
            self.poleTekstowe.insert(0, aktualnaLiczbaWPolu+liczba)

        self.poleTekstowe.configure(state = DISABLED)

    def usonOstatniZnak(self):
        """Metoda usówa ostatni znak z prawej strony ciągu pola tekstowego"""
        self.poleTekstowe.configure(state = NORMAL)
        if len(self.poleTekstowe.get()) == 1:
            self.poleTekstowe.delete(0, END)
            self.poleTekstowe.insert(0, 1)
        else:
            self.poleTekstowe.delete(len(self.poleTekstowe.get())-1, END)
            self.wyczyszczonePoleTekstowe = True

        self.poleTekstowe.configure(state = DISABLED)

    def wyczyscPole(self):
        """Metoda czyści pole tekstowe i ustawia wartość na 1"""
        self.poleTekstowe.configure(state=NORMAL)
        self.poleTekstowe.delete(0, END)
        self.poleTekstowe.insert(0, 1)
        self.poleTekstowe.configure(state=DISABLED)
        self.wyczyszczonePoleTekstowe = True

    def ukryjNastepnyKlientIRozpocznij(self):
        """Metoda ukrywa przycisk 'Następny klient' oraz rozpoczyna program"""
        self.nastepnyKlient.place_forget()
        self.startFunkcja()

    def pokazNastepnyklient(self):
        """Metoda pokazuje przycisk 'Nastepny klient'"""
        self.przyciskNaTowar.pack_forget()
        self.nastepnyKlient.place(x=170, y=210, height=60, width=150)


    def pokazTowar(self, text):
        """Metoda pokazująca kolejny towar w locowym miejscu ekranu"""
        self.przyciskNaTowar['text'] = text
        wspX=random.randint(0, 330)
        wspY=random.randint(0, 420)
        self.przyciskNaTowar.place(x=wspX, y=wspY, height=60, width=150)

    def pokazPrzegralesInformacje(self, wynikSrednia):
        """Metoda wyświetla informacje o przegranej"""
        self.poleTekstowe.place_forget()
        self.przyciskNaTowar.place_forget()
        self.wyczysc.place_forget()
        self.backspace.place_forget()
        self.zwaz.place_forget()
        for i in range(10):
            self.finallyCreatedButton[i].place_forget()

        self.ramkaStracone.place(x=0, y=0, height=500, width=1000)

    def pokazKoniecInformacje(self, wynikSrednia):
        """Metoda wyświetla informacje o końcu programu"""
        self.ramkaKoncowe.place(x=0, y=0, height=500, width=1000)
        self.poleTekstowe.place_forget()
        self.przyciskNaTowar.place_forget()
        self.wyczysc.place_forget()
        self.backspace.place_forget()
        self.zwaz.place_forget()
        for i in range(10):
            self.finallyCreatedButton[i].place_forget()

        self.ramkaKoncowe.place(x=0, y=0, height=500, width=1000)
        self.czas.configure(text='Czas kasowanai jednego przedmiotu: '+str(wynikSrednia)+' s')


    def ukryjPrzegralesInformacje(self):
        """Metoda ukrywa informacje o przegranej"""
        self.ramkaStracone.pack_forget()
        self.przegrales.place_forget()
        self.sprobujPonownie.place_forget()
        self.info.place_forget()

    def ukryjKoniecInformacje(self):
        """Metoda ukrywa informacje o końcu programu"""
        self.ramkaKoncowe.pack_forget()
        self.koniec.place_forget()
        self.sprobujPonownieKoniec.place_forget()
        self.czas.place_forget()

    def sprobujPonownieFunkcja(self):
        """Metoda rozpoczyna ponownie program po przegranej"""
        self.wyczyscPole()
        self.ukryjPrzegralesInformacje()
        self.pokazNastepnyklient()
        #self.liniaPionowa: Canvas.grid()
        self.poleTekstowe.place(x=600, y=50, height=50, width=300)

        positionX = 660
        positionY = 80
        for i in range(10):
            if i % 3 == 0:
                positionY += 60
                positionX = 600
            self.finallyCreatedButton[i].place(x=positionX, y=positionY, height=60, width=60)
            positionX += 60
        positionX = 600
        #positionY += 60
        self.finallyCreatedButton[len(self.finallyCreatedButton) - 1].place(x=positionX, y=positionY, height=60, width=180)

        self.wyczysc.place(x=780, y=140, height=60, width=120)
        self.backspace.place(x=780, y=200, height=60, width=120)
        self.zwaz.place(x=780, y=260, height=120, width=120)

    def sprobujPonownieKoniecFunkcja(self):
        """Metoda rozpoczyna ponownie program po wygranej"""
        self.wyczyscPole()
        self.ukryjKoniecInformacje()
        self.pokazNastepnyklient()

        self.poleTekstowe.place(x=600, y=50, height=50, width=300)

        positionX = 660
        positionY = 80
        for i in range(10):
            if i % 3 == 0:
                positionY += 60
                positionX = 600
            self.finallyCreatedButton[i].place(x=positionX, y=positionY, height=60, width=60)
            positionX += 60
        positionX = 600
        self.finallyCreatedButton[len(self.finallyCreatedButton) - 1].place(x=positionX, y=positionY, height=60,
                                                                            width=180)

        self.wyczysc.place(x=780, y=140, height=60, width=120)
        self.backspace.place(x=780, y=200, height=60, width=120)
        self.zwaz.place(x=780, y=260, height=120, width=120)
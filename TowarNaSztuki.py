import random

from Towar import Towar


class TowarNaSztuki(Towar):
    """Klasa dziedzicząca po klasie Towar"""
    def __init__(self, towar):
        super().__init__(towar)
        self.ilosc = self.getIlosc()

    def getIlosc(self):
        """Metoda zwraca ilość towaru prawdopodobieństwem 50% na wyslosownaie towaru na sztuki lub towaru na wagę"""
        jestWiecejNizJeden = random.choice([True, False])
        return random.randint(2, 50) if jestWiecejNizJeden else 1
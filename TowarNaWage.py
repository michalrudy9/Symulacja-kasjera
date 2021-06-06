import random

from Towar import Towar


class TowarNaWage(Towar):
    """Klasa dziedzicząca po klasie Towar"""
    def __init__(self, towar):
        super().__init__(towar)
        self.waga = round(random.uniform(0.05, 2), 2)
        self.czyZwazony = False
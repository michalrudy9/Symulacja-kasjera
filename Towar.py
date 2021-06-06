import random
from datetime import datetime


class Towar:
    """Abstrakcyjn klasa bazowa dla towarów"""
    def __init__(self, towar):
        self.nazwaTowaru = random.choice(towar)
        self.czasPojawieniaSieWOknie = datetime.now()
        self.czasSkasowania = datetime.now()
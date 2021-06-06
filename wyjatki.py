class Error(Exception):
    """Klasa bazowa wyjątków"""
    pass


class TowarNieZwazonyWyjatek(Error):
    """Wyjątek rzucany w momencie gdy towar na wagę nie został zważony"""
    def __init__(self, message='Towar na wagę nie został zważony!'):
        self.message = message
        super().__init__(self.message)


class WazenieTowarNaSztukiWyjatek(Error):
    """Wyjątek rzucany gdy towar na sztuki zostaje zważony"""
    def __init__(self, message='Próba zważenia towaru na sztuki!'):
        self.message = message
        super().__init__(self.message)


class ZaDuzaWartoscPolaTekstowegoWyjatek(Error):
    """Wyjątek rzucany w momencie gdu użytkownik poda za duża warośc w polu tekstowym"""
    def __init__(self, message='Wartość pola tekstowego przewyższa liczebność towaru!'):
        self.message = message
        super().__init__(self.message)
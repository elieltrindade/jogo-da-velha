class Tabuleiro:

    def __init__(self):
        self.casa = []

    def preencherCasa(self):
        for cont in range(9):
            self.casa.append(cont+1)

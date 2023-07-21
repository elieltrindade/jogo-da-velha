import sys

class Tabuleiro:

    def __init__(self):
        self.casa = []

    def preencherCasa(self):
        for cont in range(9):
            self.casa.append(cont+1)

    def mostarTabuleiro(self):
        cont = 0
        print(f'{"+---+---+---+"}')
        for c in range(1, 4):
            for c2 in range(1, 4):
                sys.stdout.write(f'{"|"}{self.casa[cont]:^3}')
                cont += 1
            sys.stdout.write(f'{"|"}\n')
        print(f'{"+---+---+---+"}\n')
import sys

class Tabuleiro:

    def __init__(self):
        self.casa = []

    def preencherCasa(self):
        for cont in range(9):
            self.casa.append(int(cont+1))

    def mostarTabuleiro(self):
        cont = 0
        print(f'{"+---+---+---+"}')
        for c in range(1, 4):
            for c2 in range(1, 4):
                sys.stdout.write(f'{"|"}{self.casa[cont]:^3}')
                cont += 1
            sys.stdout.write(f'{"|"}\n')
        print(f'{"+---+---+---+"}\n')

    def escolherCasa(self, jogador):
        while True:
            jogada = int(input("Escolha uma casa: "))
            if jogada not in self.casa:
                print("Casa indisponível")
            else:
                self.casa[jogada-1] = str(jogador.char)
                return

    def verificaGanhador(self):
        vitoria = False
        if (self.casa[0] == self.casa[1] and self.casa[1] == self.casa[2]) or \
                (self.casa[0] == self.casa[3] and self.casa[3] == self.casa[6]) or \
                (self.casa[0] == self.casa[4] and self.casa[4] == self.casa[8]) or \
                (self.casa[1] == self.casa[4] and self.casa[4] == self.casa[7]) or \
                (self.casa[2] == self.casa[5] and self.casa[5] == self.casa[8]) or \
                (self.casa[2] == self.casa[4] and self.casa[4] == self.casa[6]) or \
                (self.casa[3] == self.casa[4] and self.casa[4] == self.casa[5]) or \
                (self.casa[6] == self.casa[7] and self.casa[7] == self.casa[8]):
            return True

class Jogador:
    def __init__(self, name, char, jogando=False):
        self.name = name
        self.char = char
        self.jogando = jogando

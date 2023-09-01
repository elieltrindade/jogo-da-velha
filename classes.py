import sys


class Tabuleiro:

    def __init__(self, rodada=9):
        self.casa = []
        self.rodada = rodada

    def preencher_casa(self):
        for cont in range(9):
            self.casa.append(int(cont + 1))

    def mostar_tabuleiro(self):
        cont = 0
        print(f'{"+---+---+---+"}')
        for c in range(1, 4):
            for c2 in range(1, 4):
                sys.stdout.write(f'{"|"}{self.casa[cont]:^3}')
                cont += 1
            sys.stdout.write(f'{"|"}\n')
        print(f'{"+---+---+---+"}\n')

    def escolher_casa(self, jogador):
        while True:
            try:
                jogada = int(input(f'{jogador.name}{" -> "}{"Escolha uma casa: "}'))

                if 1 <= jogada <= 9:
                    if self.verifica_casa(jogada):
                        self.casa[jogada - 1] = str(jogador.char)
                        return
                    else:
                        print("A casa já ocupada, escolha outra.")
                else:
                    print("Número fora do intervalo válido (1 a 9). ")
            except ValueError:
                print("Entrada inválida. Insira um número válido (1 a 9).")

    def verifica_casa(self, jogada):
        return jogada in self.casa

    def verifica_ganhador(self):
        if (self.casa[0] == self.casa[1] and self.casa[1] == self.casa[2]) or \
                (self.casa[0] == self.casa[3] and self.casa[3] == self.casa[6]) or \
                (self.casa[0] == self.casa[4] and self.casa[4] == self.casa[8]) or \
                (self.casa[1] == self.casa[4] and self.casa[4] == self.casa[7]) or \
                (self.casa[2] == self.casa[5] and self.casa[5] == self.casa[8]) or \
                (self.casa[2] == self.casa[4] and self.casa[4] == self.casa[6]) or \
                (self.casa[3] == self.casa[4] and self.casa[4] == self.casa[5]) or \
                (self.casa[6] == self.casa[7] and self.casa[7] == self.casa[8]):
            return True

    def fim_rodada(self):
        self.rodada -= 1


class Jogador:
    def __init__(self, name, char, jogando=False, start=False):
        self.name = name
        self.char = char
        self.jogando = jogando
        self.start = start

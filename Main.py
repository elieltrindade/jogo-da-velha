from tabuleiro import Tabuleiro
from jogador import Jogador


def printPlayers():
    print(j1.name, j1.char)
    print(j2.name, j2.char)


def titulo():
    pass


def inicioJogo():
    pass


def jogar():
    pass


def verificaGanhador():
    pass


tab = Tabuleiro()
j1 = Jogador('Jogador 1', 'X')
j2 = Jogador('Jogador 2', 'O')
printPlayers()
tab.preencherCasa()
print(tab.casa)

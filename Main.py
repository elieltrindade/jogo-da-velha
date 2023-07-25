from tabuleiro import Tabuleiro
from jogador import Jogador
import sys


def printLegenda(j1, j2):
    print(f'{"-"}{"JOGO DA VELHA"}{"-"}\n\n'
          f'{j1.name:10}{" - "}{j1.char}\n'
          f'{j2.name:10}{" - "}{j2.char}\n')
    return


def trocaJogador(j1, j2):
    if not j1.jogando:
        if not j2.jogando:
            j1.jogando = True
            return
        elif not j1.jogando:
            j2.jogando = False
            j1.jogando = True
            return
    j1.jogando = False
    j2.jogando = True




def jogar(jogador):
    pass


def verificaGanhador(tab):
    vitoria = False
    tab.casa[8] = "O"
    tab.casa[4] = "X"
    tab.casa[0] = "O"
    if (tab.casa[0] == tab.casa[1] and tab.casa[1] == tab.casa[2]) or \
            (tab.casa[0] == tab.casa[3] and tab.casa[3] == tab.casa[6]) or \
            (tab.casa[0] == tab.casa[4] and tab.casa[4] == tab.casa[8]) or \
            (tab.casa[1] == tab.casa[4] and tab.casa[4] == tab.casa[7]) or \
            (tab.casa[2] == tab.casa[5] and tab.casa[5] == tab.casa[8]) or \
            (tab.casa[2] == tab.casa[4] and tab.casa[4] == tab.casa[6]) or \
            (tab.casa[3] == tab.casa[4] and tab.casa[4] == tab.casa[5]) or \
            (tab.casa[6] == tab.casa[7] and tab.casa[7] == tab.casa[8]):
        vitoria = True
        print("há um vencedor")
        return vitoria


tab = Tabuleiro()
j1 = Jogador('Jogador 1', 'X')
j2 = Jogador('Jogador 2', 'O')
printLegenda(j1, j2)
tab.preencherCasa()
tab.mostarTabuleiro()
verificaGanhador(tab)
trocaJogador(j1, j2)

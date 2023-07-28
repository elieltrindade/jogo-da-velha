from classes import Tabuleiro
from classes import Jogador


def legenda(j1, j2):
    print(f'{"-"}{"JOGO DA VELHA"}{"-"}\n\n'
          f'{j1.name:10}{" - "}{j1.char}\n'
          f'{j2.name:10}{" - "}{j2.char}\n')
    

def trocaJogador(j1, j2):
    if not j1.jogando:
        if not j2.jogando:
            j1.jogando = True
            return j1
        elif not j1.jogando:
            j2.jogando = False
            j1.jogando = True
            return j1
    j1.jogando = False
    j2.jogando = True
    return j2


j1 = Jogador('Jogador 1', 'X')
j2 = Jogador('Jogador 2', 'O')
while True:
    tab = Tabuleiro()
    tab.preencherCasa()
    while True:
        legenda(j1, j2)
        tab.mostarTabuleiro()
        jogador = trocaJogador(j1, j2)
        tab.escolherCasa(jogador)
        if True == tab.verificaGanhador():
            print(f'{jogador.name} {"Venceu"}')
            break
        if int not in tab.casa:
            pass

    restart = input("jogar novamente?")
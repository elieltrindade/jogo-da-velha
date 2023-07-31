from classes import Tabuleiro, Jogador


def legenda():
    print(f'{"-"}{"JOGO DA VELHA"}{"-"}\n\n'
          f'{j1.name:10}{" - "}{j1.char}\n'
          f'{j2.name:10}{" - "}{j2.char}\n')


def joga_primeiro():
    if not j1.start:
        if not j2.start:
            j1.start = True
            j1.jogando = True
            return j1
        elif not j1.start:
            j2.start = False
            j2.jogando = False
            j1.start = True
            j1.jogando = True
            return j1
    j1.start = False
    j1.jogando = False
    j2.start = True
    j2.jogando = True
    return j2


def troca_jogador():
    if not j1.jogando:
        j2.jogando = False
        j1.jogando = True
        return j1
    j1.jogando = False
    j2.jogando = True
    return j2


def restart():
    while True:
        try:
            continuar = int(input("jogar novamente? [1]SIM, [2] NÃO: "))
            if continuar == 1:
                return True
            elif continuar == 2:
                return False
            else:
                print("opção inválida")
        except ValueError:
            print("não é uma opção válida")


j1 = Jogador('Jogador 1', 'X')
j2 = Jogador('Jogador 2', 'O')
while True:
    tab = Tabuleiro()
    tab.preencher_casa()
    jogador = joga_primeiro()
    while True:
        legenda()
        tab.mostar_tabuleiro()
        tab.escolher_casa(jogador)
        if tab.verifica_ganhador():
            print(f'{jogador.name} {"Venceu"}')
            break
        if tab.rodada == 1:
            print("Velha!!!")
            break
        tab.fim_rodada()

        jogador = troca_jogador()
    if not restart():
        break

from classes import Tabuleiro, Jogador


def legenda():
    print(f'-{" JOGO DA VELHA "}-\n\n'
          f'{jogador1.name:10} - {jogador1.char}\n'
          f'{jogador2.name:10} - {jogador2.char}\n')


def joga_primeiro():
    if not jogador1.start:
        if not jogador2.start:
            jogador1.start = True
            jogador1.jogando = True
            return jogador1
        elif not jogador1.start:
            jogador2.start = False
            jogador2.jogando = False
            jogador1.start = True
            jogador1.jogando = True
            return jogador1
    jogador1.start = False
    jogador1.jogando = False
    jogador2.start = True
    jogador2.jogando = True
    return jogador2


def troca_jogador():
    if not jogador1.jogando:
        jogador2.jogando = False
        jogador1.jogando = True
        return jogador1
    jogador1.jogando = False
    jogador2.jogando = True
    return jogador2


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


jogador1 = Jogador('Jogador 1', 'X')
jogador2 = Jogador('Jogador 2', 'O')
while True:
    tab = Tabuleiro()
    tab.preencher_casa()
    jogador = joga_primeiro()
    while True:
        legenda()
        tab.mostar_tabuleiro()
        tab.escolher_casa(jogador)
        if tab.verifica_ganhador():
            tab.mostar_tabuleiro()
            print(f'{jogador.name} {"Venceu"}')
            break
        if tab.rodada == 1:
            tab.mostar_tabuleiro()
            print("Velha!!!")
            break
        tab.fim_rodada()

        jogador = troca_jogador()
    if not restart():
        break

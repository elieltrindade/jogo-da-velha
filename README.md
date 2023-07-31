#Jogo da Velha 
Este é um simples jogo da velha em Python.

:o: :hash: :x:
## Classes
###Tabuleiro
Classe que representa o tabuleiro.

Métodos:

**__init__(self, rodada=1)**: Construtor que inicializa o tabuleiro vazio e define o número da rodada.

**preencher_casa(self)**: Preenche as casas do tabuleiro com os números de 1 a 9.

**mostrar_tabuleiro(self)**: Mostra o tabuleiro na saída do console.

**escolher_casa(self, jogador)**: permite que um jogador escolha uma casa no tabuleiro.

**verifica_ganhador(self)**: verifica se há um vencedor no jogo, retornando True caso haja.

**fim_rodada(self)**: Decrementa o número da rodada em 1.

###Jogador
Classe que representa um jogador.

Atributos:

_**name**_: nome do jogador.
_**char**_: caractere usado pelo jogador no tabuleiro (normalmente 'X' ou 'O').

_**jogando**_: Indica se é a vez do jogador jogar.

_**start**_: Indica se o jogador iniciará a partida.

##Funções
**legenda()**: exibe a legenda dos jogadores e seus caracteres no tabuleiro.

**joga_primeiro()**: decide qual jogador começa a partida.

**troca_jogador()**: troca a vez do jogador após cada jogada.

**restart()**: pergunta se os jogadores desejam jogar novamente.

##Fluxo do Jogo
As classes Tabuleiro e Jogador são definidas no início do código.

O código define algumas funções auxiliares para facilitar o controle do jogo.

Os objetos j1 e j2 são criados representando os jogadores 1 e 2, respectivamente.

O jogo entra em um loop principal, onde cada iteração corresponde a uma partida.

A cada partida, um novo tabuleiro é criado e as casas são preenchidas com os números de 1 a 9.

Um jogador é escolhido para começar a partida.

O jogo entra em outro loop, onde cada iteração corresponde a uma rodada da partida.

A legenda dos jogadores é exibida, mostrando seus nomes e caracteres.

O tabuleiro é mostrado.

O jogador da vez escolhe uma casa para fazer sua jogada.

Após a jogada, o jogo verifica se há um vencedor. Se houver, o jogo anuncia o vencedor e termina a partida.

Se não houver vencedor e todas as casas estiverem preenchidas, o jogo anuncia empate e termina a partida.

Se ainda houver casas vazias e nenhum vencedor, a rodada termina, e é a vez do próximo jogador.

O jogo verifica se os jogadores desejam jogar novamente. Se sim, o loop de partida é repetido; caso contrário, o jogo é encerrado.

##Observações
O jogo é jogado no terminal.
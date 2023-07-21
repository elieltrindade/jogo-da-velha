# Código em Portugol
# To do Refactor for python

algoritmo "JogoDaVelha2"
var
start: Caractere
tab : vetor[1..3,1..3] de Inteiro
l,c, cont, rodada, li, col, jog : inteiro
R, vitoria, empate : logico


//Verifica o numero escolhido
Procedimento verifica()
var
inicio
R <- falso
Para l <- 1 ate 3 faca
   Para c <- 1 ate 3 faca
      Se tab[l,c] = jog entao
         R <- verdadeiro
      FImSe
      Se (tab[l,c] = jog) e (rodada % 2 = 0)entao
         tab[l,c] <- 10
      senao
         se (tab[l,c] = jog) e (rodada % 2 = 1)entao
            tab[l,c] <- 11
         FimSe
      FimSe
   FimPara
FimPara
FimProcedimento

//verifica se o jogo acabou
Procedimento fimJogo()
inicio
vitoria <- falso
empate <- falso
//jogos em linha
Para l <- 1 ate 3 faca
   Se (tab[l,1] = tab[l,2]) e (tab[l,2] = tab[l,3]) entao
   vitoria<- verdadeiro
   FimSe
FimPara
//Jogos em coluna
Para c <- 1 ate 3 faca
   Se (tab[1,c]= tab[2,c]) e (tab[2,c] = tab[3,c]) entao
   vitoria<- verdadeiro
   FimSe
FimPara
//Jogos em diagonal
Se (tab [1,1] = tab[2,2]) e (tab[2,2] =  tab[3,3]) entao
    vitoria<- verdadeiro
FimSe
Se (tab[1,3] = tab[2,2]) e (tab [2,2] = tab[3,1]) entao
   vitoria <- verdadeiro
FimSe
Se (rodada = 9) e (vitoria = falso) entao
   Empate <- verdadeiro
FimSe
FimProcedimento

//Mostra o resultado do jogo
Procedimento resultado()
inicio
Se ( vitoria = verdadeiro) e (rodada % 2 = 0) entao
   EscrevaL()
   EscrevaL("+---+---+---+")
   Para L <- 1 ate 3 faca
      Para C <- 1 ate 3 faca
         Se (tab[l,c] = 10) entao
            Escreva("| O ")
         senao
            Escreva("|   ")
         FimSe
      FimPara
      Escreva("|")
      EscrevaL("")
      EscrevaL("+---+---+---+")
   FimPara
   EscrevaL("VITÓRIA DO [O]")
   EscrevaL()
Senao
   se ( vitoria = verdadeiro) e (rodada % 2 = 1) entao
      EscrevaL()
      EscrevaL("+---+---+---+")
      Para L <- 1 ate 3 faca
         Para C <- 1 ate 3 faca
            Se (tab[l,c] = 11) entao
               Escreva("| X ")
            senao
               Escreva("|   ")
            FimSe
         FimPara
         Escreva("|")
         EscrevaL("")
         EscrevaL("+---+---+---+")
      FimPara
      EscrevaL("VITÓRIA DO [X]")
      EscrevaL()
   FimSe
FimSe
se (empate = verdadeiro) entao
   EscrevaL("Deu VELHA")
   EscrevaL()
FimSe
FimSe
FimProcedimento


inicio
titulo()
EscrevaL("Iniciar jogo da velha?[S/N]")
Leia (start)
respConvert ()
Se (start = "S") entao
Enquanto (start = "S") faca
   LimpaTela
   //Preenche os espaços do vetor tab
   vitoria <- falso
   empate <- falso
   rodada <- 0
   cont <- 1
   Para L <- 1 ate 3 faca
      Para C <- 1 ate 3 faca
         tab[l,c] <- cont
         cont <- cont + 1
      FimPara
   FimPara
   Titulo()
   tabuleiro()
   // Jogadas
   Enquanto (vitoria = falso) e (empate = falso) faca
      rodada <- rodada + 1
      Repita
         Se (rodada % 2 = 1) entao
            EscrevaL("Em qual número deseja jogar [X]?")
         senao
            EscrevaL("Em qual número deseja jogar [O]?")
         FimSe
         Leia (jog)
         verifica()
         Se (R = falso) entao
            LimpaTela
            Titulo()
            tabuleiro()
            EscrevaL("POSIÇÃO JA OCUPADA!")
            EscrevaL()
         FimSe
      ate R = VERDADEIRO
      LimpaTela
      titulo()
      tabuleiro()
      fimjogo()
      Se (vitoria = verdadeiro ) ou (empate = verdadeiro)entao
         EscrevaL ("FIM DE JOGO")
         EscrevaL()
      FimSe
   FimEnquanto
   resultado()
   EscrevaL("Deseja jogar novamente? [S/N]")
   Leia (start)
   respConvert ()
   Se (start = "n") entao
      LimpaTela
      titulo()
      EscrevaL ("OBRIGADO POR TER JOGADO, ATÉ MAIS...")
   FimSe
FimEnquanto
senao
LimpaTela
titulo()
Escreva("Que pena, Então fica para uma próxima!")
EscrevaL()
FimSe
fimalgoritmo
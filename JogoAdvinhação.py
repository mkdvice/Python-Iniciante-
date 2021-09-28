import random # importação de número aleatório

def jogar(): #função jogar

    print("---------------------------------") #Inicio do game
    print("Bem vindo ao jogo de advinhação!")
    print("---------------------------------")

    numero_secreto = random.randrange(1,51) #definindo um o número secreto de 1 a 50
    total_de_tentativas = 0 #número de tentativas
    pontos = 1000 # pontos aparecerão no fim do game

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: ")) #entrada da dificuldade do game

    if(nivel == 1): # 1 igual a fácil
        total_de_tentativas = 20
    elif(nivel == 2):   # 2 dois é igual médio
        total_de_tentativas = 10
    else:   # > 5 será dificil
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1): # Loop para as rodadas
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        chute_str = input("Digite um número entre 1 e 50: ") # entrada do chute
        print("Você digitou " , chute_str) #mostra o chute
        chute = int(chute_str) #converte chute para número inteiro

        if(chute < 1 or chute > 50):
            print("Você deve digitar um número entre 1 e 50!")
            continue

            ''' if mostrará os números que devem serem digitados o game '''

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        '''
        
         Variáveis para mostrar se acertou ou não
         acertou é para caso o usúario tenha acertado o número secreto
         maior é para caso tenha digitado um número maior do que o secreto
         menor é para caso tenha digitado um número menor do que o secreto
         
         '''

        if(acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break

            ''' Se o usuário acertar será o programa chegará ao fim  '''

        else:
            if(maior):
                print("Você errou! O seu chute foi maior do que o número secreto.")

                ''' Se o número for maior o programa dará uma dica '''

            elif(menor):
                print("Você errou! O seu chute foi menor do que o número secreto.")

                ''' Se o número for menor o programa dará uma dica '''

            pontos_perdidos = abs(numero_secreto - chute) #cálculo para números perdidos
            pontos = pontos - pontos_perdidos #cálculo para mostrar pontos feitos no jogo

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()

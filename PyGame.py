import random

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

#valores principais
numero_secreto = random.randrange(1,101)
total_de_tentativas = 0
pontos = 1000

#seleção de dificuldade
print("Qual nível de dificuldade ?")
print("(1) Fácil (2) Médio (3) Difícil")

nivel = int(input("Defina um nivel: "))

if(nivel == 1):
    total_de_tentativas = 20
elif(nivel == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

#inicio do ciclo vicioso
for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute_str = input("Digite um número entre 1 e 100: ")
    print("Você digitou " , chute_str)
    chute = int(chute_str)

    if(chute < 1 or chute > 100):
        print("Você precisa digitar um número entre 1 e 100!")
        continue
            
#parametros
    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

#respostas
    if(acertou):
        print("Você acertou e fez {} pontos! ".format(pontos))
        break
    else:
        if(maior):
            print("Errou, chutou muito alto.")
        elif(menor):
            print("Errou, seu chute foi menor do que o número secreto.")
#sistema de pontuação
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos

print("Fim do jogo")
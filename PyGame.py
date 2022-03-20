print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

#valores principais
numero_secreto = 42
total_de_tentativas = 3

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
        print("Você acertou!")
        break
    else:
        if(maior):
            print("Errou, chutou muito alto.")
        elif(menor):
            print("Errou, seu chute foi menor do que o número secreto.")

print("Fim do jogo")
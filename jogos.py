import forca
import advinhacao

def escolhe_jogo():

    print("*********************************")
    print("********Escolha o jogo!**********")
    print("*********************************")

    print("(1)Forca (2) Advinhação")

    jogo = int(input("Qual jogo gostaria de jogar ? "))

    if(jogo == 1):
        print("Jogo da forca")
        forca.jogar()

    elif(jogo == 2):
        print("Jogo da Advinhação")
        advinhacao.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()
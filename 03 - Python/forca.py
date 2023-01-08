
def jogar():
    print("*" * 35)
    print("Bem vindo no jogo de Forca!")
    print("*" * 35)

    palavra_secreta = "banana".upper()
    letras_acertadas = ["_" for letra in palavra_secreta]




    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while(not enforcou and not acertou):
        chute = input("Qual a letra?")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1
            print(letras_acertadas)
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas

        print("jogando...")

    if(acertou):
        print("Você ganhou!!")
    else:
        print("Você perdeu!!")
    print("Fim do jogo!")

if(__name__ ==  "__main__"):
    jogar()
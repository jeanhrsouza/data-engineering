print("*" * 35)
print("Bem vindo no jogo de Adivinhação!")
print("*" * 35)


numero_secreto = 42
total_de_tentativas = 3
rodada = 1

while (rodada <= total_de_tentativas):
    print(f"Tentativa: {rodada} de {total_de_tentativas}")
    chute_str = input("Digite o seu numero: ")
    print("Você digitou: ", chute_str)
    chute = int(chute_str)

    acertou = numero_secreto == chute
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if (acertou):
        print("Você acertou!")
    else:

        if(maior):
            print("Você errou! O seu chute foi maior que o número secreto.")
        elif(menor):
            print("Você errou! O seu chute foi menor que o número secreto.")
    rodada += 1
print("Fim do jogo!")
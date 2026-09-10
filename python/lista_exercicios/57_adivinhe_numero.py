numero_secreto = 7

while True:
    tentativa = int(input("Adivinhe o número secreto entre 1 e 10: "))

    if tentativa == numero_secreto:
        print("Parabéns! Você acertou!")
        break
    print("Você errou. Tente novamente.")
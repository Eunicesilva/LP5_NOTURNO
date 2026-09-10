numero = int(input("Digite um número inteiro: "))

if numero == 0:
    print("Zero possui infinitos divisores; não é tratado neste exercício.")
else:
    numero_abs = abs(numero)
    print("Divisores:", end=" ")
    for i in range(1, numero_abs + 1):
        if numero_abs % i == 0:
            print(i, end=" ")
    print()
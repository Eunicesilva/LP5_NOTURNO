while True:
    numero = float(input("Digite um número: "))
    if numero < 0:
        print("Número negativo inserido. Encerrando.")
        break
    print("Número aceito:", numero)
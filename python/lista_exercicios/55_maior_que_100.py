while True:
    numero = float(input("Digite um número maior que 100: "))
    if numero > 100:
        print("Número válido:", numero)
        break
    print("Valor inválido. Digite um número maior que 100.")
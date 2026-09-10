soma = 0

while True:
    numero = float(input("Digite um número (0 para encerrar): "))
    if numero == 0:
        break
    soma += numero

print("Soma:", soma)
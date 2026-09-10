import random

numeros = [random.randint(1, 100) for _ in range(10)]

print("Lista:", numeros)
print("Múltiplos de 3:", [numero for numero in numeros if numero % 3 == 0])
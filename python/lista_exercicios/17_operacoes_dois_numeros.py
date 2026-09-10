a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))

print("Soma:", a + b)
print("Subtração:", a - b)
print("Multiplicação:", a * b)

if b != 0:
    print("Divisão:", a / b)
else:
    print("Divisão: não é possível dividir por zero.")
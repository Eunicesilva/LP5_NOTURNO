operacao = input("Digite a operação (+, -, *, /): ").strip()
a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))

if operacao == "+":
    resultado = a + b
elif operacao == "-":
    resultado = a - b
elif operacao == "*":
    resultado = a * b
elif operacao == "/":
    if b == 0:
        print("Não é possível dividir por zero.")
        raise SystemExit
    resultado = a / b
else:
    print("Operação inválida.")
    raise SystemExit

print("Resultado:", resultado)
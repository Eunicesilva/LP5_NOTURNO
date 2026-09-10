nota = float(input("Digite uma nota de 0 a 10: "))

if 0 <= nota < 5:
    print("Baixa")
elif nota < 7:
    print("Média")
elif nota <= 10:
    print("Alta")
else:
    print("Nota inválida.")
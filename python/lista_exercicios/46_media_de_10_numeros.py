soma = 0

for i in range(10):
    soma += float(input(f"Digite o {i + 1}º número: "))

media = soma / 10
print(f"Média: {media:.2f}")
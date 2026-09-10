numeros = []

for i in range(5):
    numeros.append(float(input(f"Digite o {i + 1}º número: ")))

print("Maior número:", max(numeros))
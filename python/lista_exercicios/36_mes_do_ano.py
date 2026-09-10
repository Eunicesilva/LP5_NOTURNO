mes = int(input("Digite um número de 1 a 12: "))

meses = {
    1: "janeiro", 2: "fevereiro", 3: "março", 4: "abril",
    5: "maio", 6: "junho", 7: "julho", 8: "agosto",
    9: "setembro", 10: "outubro", 11: "novembro", 12: "dezembro"
}

print(meses.get(mes, "Mês inválido."))
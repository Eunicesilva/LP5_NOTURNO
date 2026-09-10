combustivel = input("Digite gasolina, etanol ou diesel: ").strip().lower()

# Preços de exemplo; substitua pelos valores solicitados na aula, se necessário.
precos = {
    "gasolina": 6.00,
    "etanol": 4.00,
    "diesel": 6.20
}

if combustivel in precos:
    print(f"Preço por litro: R$ {precos[combustivel]:.2f}")
else:
    print("Combustível inválido.")
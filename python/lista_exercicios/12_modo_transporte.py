transporte = input("Escolha carro, bicicleta ou a pé: ").strip().lower()

if transporte == "carro":
    print("Velocidade média considerada: 60 km/h.")
elif transporte == "bicicleta":
    print("Velocidade média considerada: 15 km/h.")
elif transporte in ("a pé", "a pe"):
    print("Velocidade média considerada: 5 km/h.")
else:
    print("Modo de transporte inválido.")
cor = input("Digite uma cor (vermelho, verde ou azul): ").strip().lower()

if cor == "vermelho":
    print("Você escolheu vermelho.")
elif cor == "verde":
    print("Você escolheu verde.")
elif cor == "azul":
    print("Você escolheu azul.")
else:
    print("Cor inválida.")
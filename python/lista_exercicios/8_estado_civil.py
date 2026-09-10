estado = input("Digite o estado civil (solteiro, casado, divorciado, viúvo): ").strip().lower()

if estado == "solteiro":
    print("Você informou que é solteiro(a).")
elif estado == "casado":
    print("Você informou que é casado(a).")
elif estado == "divorciado":
    print("Você informou que é divorciado(a).")
elif estado == "viúvo":
    print("Você informou que é viúvo(a).")
else:
    print("Estado civil inválido.")
while True:
    palavra = input("Digite uma palavra (ou 'sair' para encerrar): ")
    if palavra.strip().lower() == "sair":
        print("Programa encerrado.")
        break
    print("Você digitou:", palavra)
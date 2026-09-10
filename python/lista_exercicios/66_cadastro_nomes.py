nomes = []

while True:
    print("\n--- MENU ---")
    print("1 - Cadastrar nome")
    print("2 - Atualizar nome")
    print("3 - Excluir nome")
    print("4 - Listar todos")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        nome = input("Digite o nome: ").strip()
        if nome:
            nomes.append(nome)
            print("Nome cadastrado com sucesso.")
        else:
            print("Nome inválido.")

    elif opcao == "2":
        if not nomes:
            print("Não há nomes cadastrados.")
            continue

        for i, nome in enumerate(nomes, start=1):
            print(f"{i} - {nome}")

        try:
            indice = int(input("Digite o número do cadastro que deseja atualizar: ")) - 1
            novo_nome = input("Digite o novo nome: ").strip()
            if 0 <= indice < len(nomes) and novo_nome:
                nomes[indice] = novo_nome
                print("Nome atualizado com sucesso.")
            else:
                print("Dados inválidos.")
        except ValueError:
            print("Digite um número válido.")

    elif opcao == "3":
        if not nomes:
            print("Não há nomes cadastrados.")
            continue

        for i, nome in enumerate(nomes, start=1):
            print(f"{i} - {nome}")

        try:
            indice = int(input("Digite o número do cadastro que deseja excluir: ")) - 1
            if 0 <= indice < len(nomes):
                removido = nomes.pop(indice)
                print(f"{removido} excluído com sucesso.")
            else:
                print("Cadastro inválido.")
        except ValueError:
            print("Digite um número válido.")

    elif opcao == "4":
        if nomes:
            print("\n--- CADASTRADOS ---")
            for i, nome in enumerate(nomes, start=1):
                print(f"{i} - {nome}")
        else:
            print("Não há nomes cadastrados.")

    elif opcao == "5":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida. Programa encerrado.")
        break

    continuar = input("Deseja realizar outra operação? (s/n): ").strip().lower()
    if continuar != "s":
        print("Programa encerrado.")
        break
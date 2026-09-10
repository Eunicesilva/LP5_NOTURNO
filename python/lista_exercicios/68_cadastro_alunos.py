from itertools import count
from validacoes import validar_nome, validar_email, validar_data_nascimento

alunos = {}
gerador_matricula = count(1001)

def gerar_matricula():
    return str(next(gerador_matricula))

def cadastrar():
    try:
        nome = validar_nome(input("Nome: "))
        email = validar_email(input("E-mail: "))
        nascimento = validar_data_nascimento(input("Data de nascimento (DD/MM/AAAA): "))
    except ValueError as erro:
        print("Erro:", erro)
        return

    matricula = gerar_matricula()
    alunos[matricula] = {
        "matricula": matricula,
        "nome": nome,
        "email": email,
        "data_nascimento": nascimento
    }
    print(f"Aluno cadastrado com sucesso! Matrícula: {matricula}")

def buscar_matricula():
    matricula = input("Digite a matrícula: ").strip()
    if matricula not in alunos:
        print("Matrícula inválida ou aluno não encontrado.")
        return None
    return matricula

def listar():
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return
    print("\n--- ALUNOS ---")
    for aluno in alunos.values():
        print("-" * 35)
        print(f"Matrícula: {aluno['matricula']}")
        print(f"Nome: {aluno['nome']}")
        print(f"E-mail: {aluno['email']}")
        print(f"Data de nascimento: {aluno['data_nascimento']}")
    print("-" * 35)

def consultar():
    matricula = buscar_matricula()
    if matricula:
        aluno = alunos[matricula]
        print("\n--- ALUNO ---")
        for chave, valor in aluno.items():
            print(f"{chave.replace('_', ' ').title()}: {valor}")

def atualizar():
    matricula = buscar_matricula()
    if not matricula:
        return

    aluno = alunos[matricula]
    print("Deixe o campo vazio para manter o valor atual.")

    novo_nome = input(f"Nome [{aluno['nome']}]: ").strip()
    novo_email = input(f"E-mail [{aluno['email']}]: ").strip()
    nova_data = input(f"Data de nascimento [{aluno['data_nascimento']}]: ").strip()

    try:
        if novo_nome:
            aluno["nome"] = validar_nome(novo_nome)
        if novo_email:
            aluno["email"] = validar_email(novo_email)
        if nova_data:
            aluno["data_nascimento"] = validar_data_nascimento(nova_data)
        print("Aluno atualizado com sucesso.")
    except ValueError as erro:
        print("Erro:", erro)

def remover():
    matricula = buscar_matricula()
    if matricula:
        removido = alunos.pop(matricula)
        print(f"Aluno {removido['nome']} removido com sucesso.")

while True:
    print("\n===== SISTEMA DE ALUNOS =====")
    print("1 - Cadastrar aluno")
    print("2 - Atualizar aluno")
    print("3 - Remover aluno")
    print("4 - Listar alunos")
    print("5 - Consultar aluno por matrícula")
    print("6 - Sair")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        cadastrar()
    elif opcao == "2":
        atualizar()
    elif opcao == "3":
        remover()
    elif opcao == "4":
        listar()
    elif opcao == "5":
        consultar()
    elif opcao == "6":
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida. Tente novamente.")
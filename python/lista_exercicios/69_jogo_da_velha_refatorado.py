def exibir(tabuleiro):
    print()
    for i in range(0, 9, 3):
        print(f" {tabuleiro[i]} | {tabuleiro[i+1]} | {tabuleiro[i+2]} ")
        if i < 6:
            print("---+---+---")
    print()

def venceu(tabuleiro, jogador):
    combinacoes = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    return any(all(tabuleiro[pos] == jogador for pos in combo) for combo in combinacoes)

def jogar():
    tabuleiro = [" "] * 9
    jogador = "X"

    while True:
        exibir(tabuleiro)

        try:
            posicao = int(input(f"Jogador {jogador}, escolha 1 a 9: ")) - 1
            if not 0 <= posicao < 9:
                print("Posição inválida.")
                continue
            if tabuleiro[posicao] != " ":
                print("Essa posição já foi utilizada.")
                continue
        except ValueError:
            print("Digite um número de 1 a 9.")
            continue

        tabuleiro[posicao] = jogador

        if venceu(tabuleiro, jogador):
            exibir(tabuleiro)
            print(f"Jogador {jogador} venceu!")
            return

        if " " not in tabuleiro:
            exibir(tabuleiro)
            print("Empate!")
            return

        jogador = "O" if jogador == "X" else "X"

while True:
    jogar()
    resposta = input("Deseja jogar novamente? (s/n): ").strip().lower()
    if resposta != "s":
        print("Programa encerrado.")
        break
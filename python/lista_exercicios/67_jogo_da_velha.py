tabuleiro = [" " for _ in range(9)]

def exibir_tabuleiro():
    print()
    print(f" {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]} ")
    print("---+---+---")
    print(f" {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]} ")
    print("---+---+---")
    print(f" {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]} ")
    print()

jogador = "X"

while True:
    exibir_tabuleiro()

    try:
        posicao = int(input(f"Jogador {jogador}, escolha uma posição de 1 a 9: ")) - 1
        if not 0 <= posicao <= 8:
            print("Posição inválida.")
            continue
        if tabuleiro[posicao] != " ":
            print("Essa posição já está ocupada.")
            continue
    except ValueError:
        print("Digite um número de 1 a 9.")
        continue

    tabuleiro[posicao] = jogador

    vitoria = (
        (tabuleiro[0] == tabuleiro[1] == tabuleiro[2] != " ") or
        (tabuleiro[3] == tabuleiro[4] == tabuleiro[5] != " ") or
        (tabuleiro[6] == tabuleiro[7] == tabuleiro[8] != " ") or
        (tabuleiro[0] == tabuleiro[3] == tabuleiro[6] != " ") or
        (tabuleiro[1] == tabuleiro[4] == tabuleiro[7] != " ") or
        (tabuleiro[2] == tabuleiro[5] == tabuleiro[8] != " ") or
        (tabuleiro[0] == tabuleiro[4] == tabuleiro[8] != " ") or
        (tabuleiro[2] == tabuleiro[4] == tabuleiro[6] != " ")
    )

    if vitoria:
        exibir_tabuleiro()
        print(f"Jogador {jogador} venceu!")
        break

    if " " not in tabuleiro:
        exibir_tabuleiro()
        print("Empate!")
        break

    jogador = "O" if jogador == "X" else "X"
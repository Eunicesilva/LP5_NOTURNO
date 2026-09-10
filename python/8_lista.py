fruta = 'Uva'

frutas = ['Maça', 'Laranja', 'Morango', 'Kiwi']

# prontando cada fruta individual

print(frutas[2])

# printando lista completa

for fruta in frutas:
    print(fruta)



# Lista com enumeração

alunos = ['victor' , 'nice', 'junior', 'Erika']

for indice, aluno in enumerate(alunos):
    print(indice, aluno)
    if indice == 2:
        print(f'O aluno {aluno} é linda')
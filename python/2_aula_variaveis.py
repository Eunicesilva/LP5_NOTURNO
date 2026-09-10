# Variaveis:

nome = 'Nice'
idade = 33
altura = 1.67
vivo = True
nascimento = 1993-12-15

# Verificação conteudo da variavel

print(nome)
print(idade)
print(altura)
print(vivo)
print(nascimento)

# Concatenando informações

print('Meu nome é :', nome)
print('Sua altura é:', altura)
print(f'sua idade é {idade}')
print(f'sua altura é {altura} sua idade é {idade} voce está vivo{vivo} Meu nome é {nome} Eu nasci em {nascimento}' )


# Verificando o tipo de variação

print(f' Meu nome é {type(nome)}')
print(type(idade))
print(type(vivo))
print(type(altura))
print(type(nascimento))

# Exemplos de uso de metodos de uma classe

print(f'conteudo original: {nome}')
print(f'conteudo em MAIUSCULO: {nome.upper()}')
print(f'conteudo captalize: {nome.capitalize()}')
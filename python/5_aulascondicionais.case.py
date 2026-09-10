# CASE
numero1 = 1
numero2 = 5

opcao = 2

match opcao:
    case 1:
        print(f' a soma é {numero1+numero2}')
    case 2:
            print(f' a soma é {numero1-numero2}')
    case 3:
            print(f' a soma é {numero1*numero2}')
    case 4:
            print(f' a soma é {numero1/numero2}')
    case _:
            print('opção invalida')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print('        EXERCÍCIO 59')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

opcao = ''

n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))

while opcao != '5':
    
    print('''\n
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR DO PROGRAMA''')
    
    opcao = input('Informe a opção que deseja : ')

    if opcao == '1':
        print(f'\n{n1} + {n2} = {n1 + n2}')
    elif opcao == '2':
        print(f'\n{n1} x {n2} = {n1 * n2}')
    elif opcao == '3':
        if n1 > n2:
            print(f'\nO maior entre eles é {n1}.')
        else:
            print(f'\nO maior entre eles é {n2}.')
    elif opcao == '4':
        n1 = int(input('\nInforme o primeiro número: '))
        n2 = int(input('Informe o segundo número: '))
    else:
        break

print('\nFim do programa!')
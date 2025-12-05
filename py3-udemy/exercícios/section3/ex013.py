# Lista de compras
# Aula 91-92

lista = []

while True:
    print(f'''\nSELECIONE SUA OPÇÃO:
[I]nserir   [A]pagar   [L]istar   [S]air''')
    while True:
        escolha = input('Digite sua opção [I/A/L/S]: ').upper()
        if escolha in 'IALS':
            break
        else:
            print('Digite uma opção válida. ', end='')
            continue

    if escolha == 'I':
        produto = input('\nProduto: ')
        lista.append(produto)

    elif escolha == 'A':
        while True:
            try:
                indice = int(input('\nDigite o índice do produto q deseja remover : '))
            except:
                print('Digite uma opção válida. ', end='')
            
            if indice > len(lista):
                print('Digite um indice existente. ', end='')
                continue
            elif indice == len(lista):
                indice -= 1
            else:
                break

        del lista[indice]

    elif escolha == 'L':
    
        if len(lista) == 0:
            print()
            print('Não houveram produtos cadastrados.')
        else:
            print()
            for i, nome in enumerate(lista):
                print(f'{i} - {nome}')

    else:
        print('Saindo...')
        break
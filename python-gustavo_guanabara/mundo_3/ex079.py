lista = []

while True:
    num = int(input('Digite um valor : '))

    if num in lista:
        print(f'Valor duplicado! Não adicionado...')
    else:
        lista.append(num)
        print("Valor adicionado com sucesso.")

    opc = input('Deseja continuar ? [S/N] ').upper()
    if opc == 'N':
        break

print(f'Os valores adicionados foram {sorted(lista)}')
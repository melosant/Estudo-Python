boletim = []
temp = []

print('=-' * 11)
print('   BOLETIM ESCOLAR')
print('=-' * 11)

while True:
    media = 0
    temp.append(str(input('\nNome : ').capitalize()))
    temp.append(float(input('Nota 1 : ')))
    media += temp[1]
    temp.append(float(input('Nota 2 : ')))
    media += temp[2]
    media /= 2
    temp.append(media)

    boletim.append(temp[:])
    temp.clear()

    resp = str(input('Deseja continuar [S/N] : ')).upper()
    if resp == 'N':
        break

print()
print('=-' * 20)
print(f'No', end=' ')
print(f'NOME', end='                          ')
print(f'MÉDIA')
print('=-' * 20)
for aluno in boletim:
    print(f'{boletim.index(aluno):<3}', end='')
    print(f'{aluno[0]:<30}', end='')
    print(f'{aluno[3]:.2f}')
print('=-' * 20)

while True:
    opc = int(input('\nMostrar as notas de qual aluno (No. / 999 para parar) : '))
    if opc == 999:
        break
    elif opc >= 0:
        for aluno in boletim:
            if opc == boletim.index(aluno):
                print('-=' * 15)
                print(f'{aluno[0]} | NOTA 1: {aluno[1]} / NOTA 2: {aluno[2]}')
                print('-=' * 15)
                continue
    else:
        print('Por favor, digite uma opção válida. ', end='')

print('\nFim do programa!')
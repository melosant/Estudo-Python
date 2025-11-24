boletim = []
temp = []

while True:
    media = 0
    temp.append(str(input('Nome : ').capitalize()))
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
    opc = int(input('Mostrar as notas de qual aluno (No. / 999 para parar) : '))
    if opc == 999:
        break
    elif opc == 
termo = int(input('Digite o primeiro termo da PA : '))
razao = int(input('Informe a razão para esta PA : '))

print('-=-=-=-=-=-=-=-=-=-')
print(f'     P.A de {termo}')
print('-=-=-=-=-=-=-=-=-=-')

print(f'\n{termo}')
for i in range(9):
    print(termo + razao)
    termo += razao
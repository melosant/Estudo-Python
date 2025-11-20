# refazendo ex051 com while
termo = int(input('Digite o primeiro termo da PA : '))
razao = int(input('Informe a razão para esta PA : '))
n = 1

print('-=-=-=-=-=-=-=-=-=-')
print(f'     P.A de {termo}')
print('-=-=-=-=-=-=-=-=-=-')

print(f'\n{termo}')
while n < 10:
    print(termo + razao)
    termo += razao
    n += 1
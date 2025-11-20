# melhorando ex061
termo = int(input('Digite o primeiro termo da PA : '))
razao = int(input('Informe a razão para esta PA : '))
c = 1
n = 10
resp = 1

print('-=-=-=-=-=-=-=-=-=-')
print(f'     P.A de {termo}')
print('-=-=-=-=-=-=-=-=-=-')

print(termo)
while str(resp) != '0':
    while c < n:
        print(termo + razao)
        termo += razao
        c += 1
    resp = int(input('Deseja calcular mais quantos termos (0 para parar): '))
    n += resp

print('Fim do programa.')
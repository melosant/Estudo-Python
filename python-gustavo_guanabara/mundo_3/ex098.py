from time import sleep

def linha():
    print('=-' * 40)

def contador(i, f, p):
    for i in range(i, f, p):
        print(i, end=' ')
        sleep(0.5)
    print('FIM!')

linha()
print('Contagem de 1 até 10 de 1 em 1: ')
contador(1, 11, 1)
linha()
print('COntagem de 10 até 0 de 2 em 2: ')
contador(10, 0, -2)
linha()
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início : '))
fim = int(input('FInal : '))
passo = int(input('Passo da contagem : '))
print(f'COntagem de {inicio} até {fim} de {passo} em {passo}: ')

if fim < inicio:
    fim -= 1
    if passo > 0:
        passo *= -1
    elif passo == 0:
        passo = -1
else:
    fim += 1
if passo == 0:
    passo = 1

contador(inicio, fim, passo)
linha()
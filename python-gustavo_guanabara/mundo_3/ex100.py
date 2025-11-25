from random import randint

def sorteio(n):
    print('\nSorteando 5 valores : ', end='')
    for i in range(5):
        num = randint(0, 10)
        n.append(num)
        print(num, end=' ')
    print('PRONTO!')

def somaPar(n):
    s = 0
    for i in n:
        if i % 2 == 0:
            s += i
    print(f'\nA soma dos valores pares de {n} é {s}.')


numeros = list()
sorteio(numeros)
somaPar(numeros)
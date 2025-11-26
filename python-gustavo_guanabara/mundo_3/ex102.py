# Programa 102 : fatorial com funções
# Funções / Escopo de Variáveis (Aula 21)

def fatorial(n, show=False):
    """
    param n - numero a ser calculado
    param show(opcional) - mostrar ou não o calculo
    return fat - retorna o fatorial
    """
    fat = 1
    print('-' * 40)
    for i in range(n, 0, -1):
        fat *= i
        if show == True:
            if i > 1:
                print(f'{i} x', end=' ')
            else:
                print(f'{i} = ', end='')
    return fat

num = int(input('Digite o número que deseja ver o fatorial : '))
print(fatorial(num, True))
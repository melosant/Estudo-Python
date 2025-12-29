def recursiva(inicio=0, fim=5):
    '''
    cria um 'loop' de recursão da própria função
    '''
    print('inicio: ', inicio, 'fim: ', fim)

    # caso base
    if inicio >= fim:
        return fim
    
    # caso recursivo
    # conta até chegar ao fim
    inicio += 1
    return recursiva(inicio, fim) # chama a propria função até a condição ser atendida

recursiva()


# fatorial recursiva
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))
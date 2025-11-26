from ex111_112pack.moedas import moedas

def leiaDinheiro(msg):
    while True:    
        n = input(f'{msg}')
        if n.isnumeric():
            break   
        else:
            print('Digite um preço válido.', end=' ')
    
    return float(n)
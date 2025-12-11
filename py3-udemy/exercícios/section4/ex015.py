# Multiplicação de argumentos não nomeados
# Aula 114

def multiplicador(*args):
    total = 1
    for n in args:
        total *= n

    return total

total = multiplicador(7,7,7)
print(total)
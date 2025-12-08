# Par ou ímpar com funções
# Aula 114

def parouimpar(num):
    if num % 2 == 0:
        return f'{num} é PAR'
    return f'{num} é ÍMPAR'
    
print(parouimpar(17))
print(parouimpar(8))
print(parouimpar(157))
print(parouimpar(228))
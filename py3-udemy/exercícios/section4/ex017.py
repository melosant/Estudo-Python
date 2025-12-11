# Dobro, Triplo e Quadruplo
# Aula 119

def criar_multiplicador(multiplicador):
    def multiplicar(num):
        return f'{num} x {multiplicador} = {num * multiplicador}'
    return multiplicar # retorna sem executar

dobro = criar_multiplicador(2)
triplo = criar_multiplicador(3)
quadruplo = criar_multiplicador(4)

print(dobro(8))
print(triplo(8))
print(quadruplo(8))
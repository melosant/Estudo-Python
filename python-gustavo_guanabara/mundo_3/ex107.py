# Programa 107 : Usando pacotes para operações aritméticas
# Modularização e Pacotes (Aula 22)

from ex107_110pack import moeda

p = float(input('Digite o preço : R$'))
print(f'''
A metade de {p} é {moeda.metade(p)}.
O dobro de {p} é {moeda.dobro(p)}.
Aumentando 10% em {p} fica {moeda.aumentar(p, 10)}
Diminuindo 13% em {p} fica {moeda.diminuir(p, 13)}''')
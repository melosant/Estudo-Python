# Programa 109 : Formatando moeda do ex107 pt 2 
# Modularização e Pacotes (Aula 22)

from ex107_110pack import moeda

p = float(input('Digite o preço : R$'))
print(f'''
A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}.
O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}.
Aumentando {10}% em {moeda.moeda(p)} fica {moeda.aumentar(p, 10, True)}
Diminuindo 13% em {moeda.moeda(p)} fica {moeda.diminuir(p, 13, True)}''')
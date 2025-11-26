# Programa 108 : Formatando moeda do ex107
# Modularização e Pacotes (Aula 22)

from ex107_110pack import moeda

p = float(input('Digite o preço : R$'))
print(f'''
A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}.
O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}.
Aumentando 10% em {moeda.moeda(p)} fica {moeda.moeda(moeda.aumentar(p, 10))}
Diminuindo 13% em {moeda.moeda(p)} fica {moeda.moeda(moeda.diminuir(p, 13))}''')
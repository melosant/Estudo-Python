# Programa 111 : Simplificando o resumo de informações
# Modularização e Pacotes (Aula 22)

from ex111pack.moedas import moedas
from ex111pack.dados import dados

p = float(input('Digite o preço : R$'))
moedas.resumo(p, 80, 35)
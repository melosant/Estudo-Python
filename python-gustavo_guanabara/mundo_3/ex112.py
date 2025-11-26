# Programa 112 : Verificação da entrada do usuário
# Modularização e Pacotes (Aula 22)

from ex111_112pack.moedas import moedas
from ex111_112pack.dados import dados
 
p = dados.leiaDinheiro('Digite um preço : R$')
moedas.resumo(p, 80, 35)
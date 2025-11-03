# Programa 21 - Caixa Eletrônico 

# variáveis
valor = int(input("Qual valor para o saque ? R$")) # entrada valor para saque
notas50 = valor // 50 # notas de 50 (divisão inteira)
resto = valor % 50 # restante após notas de 50
notas20 = resto // 20 # notas de 20 (divisão inteira)
resto = resto % 20 # restante após notas de 20
notas10 = resto // 10 # notas de 10 (divisão inteira)
resto = resto % 10 # restante após notas de 10
moedas1 = resto # moedas são o resto de 10

# impressão totais
print(f"""
VALOR DO SAQUE : R${valor}
NOTAS DE R$50 : {notas50}
NOTAS DE R$20 : {notas20}
NOTAS DE R$10 : {notas10}
MOEDAS DE R$1 : {moedas1}""")
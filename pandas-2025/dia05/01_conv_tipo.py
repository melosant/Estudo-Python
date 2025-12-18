import pandas as pd

df = pd.read_csv('pandas-2025/data/clientes.csv', sep=';')
# conversão de tipo (virou float e dps str)
print(df['qtdePontos'].astype(float).astype(str))

print()

# conversão em data 
print(pd.to_datetime(df['DtCriacao']))
# caso haja alguma data com erro ou algo que queira mudar, é possível substitui la por uma data válida com replace
# ele devolve uma série nova alterada, caso queria mudar a mesma, terá q reatribuir
# fiz a mudanças das linhas 1,2 e 3
print()
df['DtCriacao'] = pd.to_datetime(df['DtCriacao'].replace({'2024-02-01 00:00:00.000':'2025-12-18 10:00:00.000'}))

print()
# método em cima das datas
print(df['DtCriacao'].dt.date)
print(df['DtCriacao'].dt.month)
print(df['DtCriacao'].dt.year)
import pandas as pd

df = pd.DataFrame({
    'nome': ['teo', 'lara', 'nah', 'bia', 'mah', 'lara', 'mah', 'mah'],
    'sobrenome': ['calvo',  'calvo', 'ataide', 'ataide', 'silva', 'silva', 'silva', 'silva'],
})

# mantém a primeira, e remove as duplicatas apóe elas
print(df.drop_duplicates())
print()
# manter a última
print(df.drop_duplicates(keep='last'))

df1 = pd.DataFrame({
    'nome': ['teo', 'lara', 'nah', 'bia', 'mah', 'lara', 'mah', 'mah'],
    'sobrenome': ['calvo',  'calvo', 'ataide', 'ataide', 'silva', 'silva', 'silva', 'silva'],
    'salario': [2132, 1231, 454, 6543, 6532, 4322, 987, 2134]
})

print()
# dropa as duplicatas de nome e sobrenome do df ordenado e mantém o último com base na ordenação
df1 = (df1.sort_values('salario', ascending=False)
          .drop_duplicates(keep='last', subset=['nome', 'sobrenome']))

print(df1)
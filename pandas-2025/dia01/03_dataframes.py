import pandas as pd

idades = [
    32, 38, 30, 30, 31,
    35, 25, 29, 31, 37,
    27, 23, 36, 33, 39
]

nomes = [
    'Teo', 'Maria', 'Nathã', 'Jose', 'Luis',
    'Ana', 'Nah', 'Dani', "Mah", 'Fer',
    'Nanda', 'Naty', 'Pedro', 'Kozato', 'Kozato'
]

series_idades = pd.Series(idades)
series_nomes = pd.Series(nomes)

# dataframe funciona como um conjunto de séries
# se series navega por linhas, o df é uma matrix ixj
df = pd.DataFrame()
df['idades'] = series_idades
df['nomes'] = series_nomes
print(df)

print()

# acessa as series 
# os indices sao os indices do df
print(df['nomes'])
print(df['idades'])

print()

# retorna uma serie a nivel linha
# onde os indices sao os nomes das colunas do df
print('Iloc na posição 0: ', df.iloc[0])
print('Nome na posição 0: ', df.iloc[0]['nomes'])
print('Idade da última pessoa : ', df.iloc[-1]['idades'])
import pandas as pd

idades = [
    32, 38, 30, 30, 31,
    35, 25, 29, 31, 37,
    27, 23, 36, 33, 39
]

# os indices funcionam como keys nos dicts, não como as listas
series_idades = pd.Series(idades)
print(series_idades)
print('Índice 0: ', series_idades[0])
# print(series_idades[-1]) vai dar erro

print()

# ordenando os values
# o indice fica vinculado a um valor na series, não mudando mesmo ordenando
series_idades = series_idades.sort_values()
print(series_idades)
print('Índice 0 pós-ordenar: ', series_idades[0])

print()

# iloc permite usar os indices como posiçoes e não como keys
# iloc navega nas linhas!!!!!!
print('Iloc Índice 0: ', series_idades.iloc[0])
print('Iloc Índice -1: ', series_idades.iloc[-1])
print('Slice 3 primeiros: ', series_idades.iloc[:3])

print()

# setando indexs
idades = [
    32, 38, 30, 30, 31,
    35, 25, 29, 31, 37,
    27, 23, 36, 33, 39
]

indexs = [
    'Teo', 'Maria', 'Nathã', 'Jose', 'Luis',
    'Ana', 'Nah', 'Dani', "Mah", 'Fer',
    'Nanda', 'Naty', 'Pedro', 'Kozato', 'Kozato'
]

series_idades1 = pd.Series(idades, index=indexs)
print(series_idades1)

print()

print('Valor indice Nathã: ', series_idades1['Nathã'])
print('Valor posição 0: ', series_idades1.iloc[0])
print('Todos os valores de Kozato: \n',series_idades1['Kozato'])

# loc navega pelos índices (na series já se faz isso, então é possível ocultar)
print('Valor de Teo usando .loc: ', series_idades1.loc['Teo'])
import pandas as pd

idades = [
    32, 38, 30, 30, 31,
    35, 25, 29, 31, 37,
    27, 23, 36, 33, 39
]

# media = sum(idades) / len(idades)
# diffs = 0
# for i in idades:
#     diffs += (i - media) ** 2
# variancia = diffs / (len(idades) - 1)

series_idades = pd.Series(idades)
print(series_idades)

# stats da series
print('\nMédia: ', series_idades.mean())
print('\nVariância: ', series_idades.var())
print('\nSumário: ', series_idades.describe())
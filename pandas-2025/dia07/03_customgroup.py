import pandas as pd
import numpy as np

transacoes = pd.read_csv('pandas-2025/data/transacoes.csv', sep=';')

def diff_amp(x: pd.Series):
    amplitude = x.max() - x.min()
    media = x.mean()
    return np.sqrt((amplitude - media) ** 2)

def life_time(x: pd.Series):
    dt = pd.to_datetime(x)
    return (dt.max() - dt.min()).days

idades = pd.Series([21, 26, 45, 55, 21, 18, 64, 11, 28, 17])
# aplica a função customizada na serie
print(diff_amp(idades))

# aplica as funções customizadas nas series do df
sumario = (transacoes.groupby(by=['IdCliente'], as_index=False)
           .agg({
                'IdTransacao': ['count'],
                'QtdePontos': ['sum', 'mean', diff_amp],
                'DtCriacao': [life_time]})
            )

sumario.columns = ['IdCLiente', 'QtdeTransacao', 'TotalPontos', 'AvgPontos', 'AmpMeanDiff', 'LifeTime']
print(sumario)
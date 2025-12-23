import pandas as pd

df = pd.read_csv('pandas-2025/dia10/homicidios-consolidado.csv', sep=';')

# defino os índices e faço a stack, ele retorna como uma serie
df_stack = (df.set_index(['nome', 'período'])
              .stack())

# reseto os índices para transformar em df e renomeio as colunas
df_stack = df_stack.reset_index()
df_stack.columns = ['nome', 'período', 'métrica', 'valor']
print(df_stack)

# para desempilhar, seto os índices, desempilho e reseto os índices
df_unstack = (df_stack.set_index(['nome', 'período', 'métrica'])
                      .unstack()
                      .reset_index())
print(df_unstack.head())

# para acabar com o multiIndex
# droplevel removeu os pares do multiIndex (mas ele remove nome e período)
metricas = df_unstack.columns.droplevel(0)[2:].tolist()
df_unstack.columns = ['nome', 'período'] + metricas
print(df_unstack.head())
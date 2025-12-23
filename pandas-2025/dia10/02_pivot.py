import pandas as pd

df = pd.read_csv('pandas-2025/dia10/homicidios-consolidado.csv', sep=';')

df_stack = (df.set_index(['nome', 'período'])
       .stack()
       .reset_index())
df_stack.columns = ['nome', 'período', 'métrica', 'valor']

print(df_stack)

# pivot table pós stack, é possível definir a tabela por completo
df_pivot = (df_stack.pivot_table(values='valor', 
                                index=['nome', 'período'], 
                                columns='métrica')
                    .reset_index())

print(df_pivot)

# ignora o período e faz a média dos casos nos períodos
df_pivot_mean = (df_stack.pivot_table(values='valor',
                                      index=['nome'],
                                      columns='métrica',
                                      aggfunc='mean')
                         .reset_index())

print(df_pivot_mean)

# ----------- PARA VOLTAR PARA STACK ------------------
# df_pivot_mean = (df_stack.pivot_table(values='valor',
#                                       index=['nome'],
#                                       columns='métrica',
#                                       aggfunc='mean')
#                          .reset_index()
#                          .stack())
# print(df_pivot_mean)
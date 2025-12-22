import pandas as pd
import os

# função que le, renomeia coluna, define índice e remove coluna em comum
def read_file(filename:str):
    df = pd.read_csv(f'pandas-2025/data/ipea/{filename}.csv', sep=';')
    df = df.rename(columns={'valor':filename})
    df = df.set_index(['nome', 'período'])
    df = df.drop(['cod'], axis=1)
    
    return df

filenames = os.listdir('pandas-2025/data/ipea/') # todos os arquivos do diretorio
dfs = []
for i in filenames: # itera sobre os nomes do arquivo e passa como parâmetro para função 
    file_name = i.split('.')[0]
    dfs.append(read_file(file_name))

df_full = (pd.concat(dfs, axis=1) # concatena todos os dfs da lista
            .reset_index()
            .sort_values(['período', 'nome']))

df_full.to_csv('pandas-2025/dia08/homicidios-consolidado.csv', index=False, sep=';')

print(df_full)
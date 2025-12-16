import pandas as pd

clientes = pd.read_csv('pandas-2025/data/clientes.csv', sep=';')

# maior valor
max_ponto = clientes['qtdePontos'].max()
filtro = clientes['qtdePontos'] == max_ponto
print(clientes[filtro])

# ordenando a serie x ordenando o dataframe pela serie
# retorna um dataframe novo
print(clientes['qtdePontos'].sort_values())
print(clientes.sort_values(by='qtdePontos'))
# ordem decrescente: os 5 ids dos clientes com mais pontos 
print(clientes.sort_values(by='qtdePontos', ascending=False)
              .head(5)['idCliente'])

brinquedo = pd.DataFrame(
    {
        'nome' : ['teo', 'marcos', 'nilton', 'lucas'],
        'idade' : [35, 15, 78, 55],
        'salario' : [4500, 1200, 4500, 3000],
    }
)

# ordena com base no salário DESCRESCENTE e, em caso de valores iguais, usa a idade CRESCENTE como base
print(brinquedo.sort_values(by=['salario', 'idade'], ascending=[False, True]))
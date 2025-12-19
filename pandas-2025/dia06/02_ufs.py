import pandas as pd
import requests

# --------- SSÓ PRA DAR AUTORIZAÇÃO PRA SE PASSAR POR UM NAVEGADOR ----------------
url = 'https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil'
header = {
  "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
  "X-Requested-With": "XMLHttpRequest"}
r = requests.get(url, headers=header)

dfs = pd.read_html(r.text)
uf = dfs[1]

def str_to_float(x:str):
    x = float(x.replace(' ', '')
               .replace(',', '.')
               .replace('\xa0', ''))
    return float(x)

def exp_to_year(x:str):
    x = x.split(' ')[0].replace(',', '.')
    return float(x)

def alpha_to_percent(x):
    x = x.replace(',', '.').replace('%', "")
    x = float(x) / 100
    return x

def infantil(x):
    x = x.replace(',', '.').replace('‰', '')
    return float(x)

# apply em colunas, transformando as series em floats
uf['Área (km²)'] = uf['Área (km²)'].apply(str_to_float)
uf['População (Censo 2022)'] = uf['População (Censo 2022)'].apply(str_to_float)
uf['PIB (2015)'] = uf['PIB (2015)'].apply(str_to_float)
uf['PIB per capita (R$) (2015)'] = uf['PIB per capita (R$) (2015)'].apply(str_to_float)
uf['Expectativa de vida (2016)'] = uf['Expectativa de vida (2016)'].apply(exp_to_year)
uf['Mortalidade infantil (/1000)'] = uf['Mortalidade infantil (2016)'].apply(infantil)
uf['Alfabetização (2016)'] = uf['Alfabetização (2016)'].apply(alpha_to_percent)

# criando uma nova coluna de região
def uf_to_regiao(uf):
    if uf in ['Distrito Federal', 'Goiás', 'Mato Grosso', 'Mato Grosso do Sul']:
        return 'Centro-Oeste'
    elif uf in ['Alagoas', 'Bahia' , 'Ceará' , 'Maranhão', 'Paraíba', 'Pernambuco', 'Piauí', 'Rio Grande do Norte', 'Sergipe']:
        return 'Nordeste'
    elif uf in ['Acre', 'Amapá', 'Amazonas', 'Pará', 'Rondônia', 'Roraima', 'Tocantins']:
        return 'Norte'
    elif uf in ['Espírito Santo', 'Minas Gerais', 'Rio de Janeiro', 'São Paulo']:
        return 'Sudeste'
    else:
        return 'Sul'

uf['Região'] = uf['Unidade federativa'].apply(uf_to_regiao)

# classificação por linhas
def classifica_bom(linha):
    return (linha['PIB per capita (R$) (2015)'] > 30000 and
            linha['Mortalidade infantil (/1000)'] < 15 and
            linha['IDH (2010)'] > 700)

print(uf.apply(classifica_bom, axis=1))

print(uf)
from libs.functions.func_gerais import *

def opcaoum(caminho):
    with open(caminho, 'r') as a:
        print(a.read())

def opcaodois(caminho):
    nome = leianome('\033[1;92mNome: \033[m')
    
    idade = leiaint('\033[1;92mIdade: \033[m')
    if idade == 0:
        idade_inf = '<Não Informado>'
    else:
        idade_inf = idade
    
    if nome == '<Não Informado>' and idade_inf == '<Não Informado>':
        pass
    else:
        with open(caminho, 'a') as a:
            a.write(f'  - {nome} : {idade_inf} anos de idade\n')
from libs.functions.func_gerais import *

def opcaoum(caminho):
    '''
    Função que exibe as pessoas já cadastradas.
    param caminho: caminho do arquivo onde foram cadastradas as pessoas.
    '''
    with open(caminho, 'r') as a: # with para garantir q o arquivo seja fechado após usar, e 'r' é de read.
        print(a.read())

def opcaodois(caminho):
    '''
    Função que cadastra uma nova pessoa.
    param caminho: caminho do arquivo para cadastrar as pessoas.
    '''
    nome = leianome('\033[1;92mNome: \033[m') # cadastro do nome (usando função leianome feita em \func_gerais)
    
    idade = leiaint('\033[1;92mIdade: \033[m') # cadastro da idade (usando função leiaint feita em \fun_gerais)
    
    if idade == 0: # se idade for = 0, substitui por Não Informada
        idade_inf = '<Não Informado>'
    else:
        idade_inf = idade # senão, recebe o literal inteiro.
    
    if nome == '<Não Informado>' and idade_inf == '<Não Informado>':
        pass # se nada for informado, não adiciona ao arquivo
    else:
        with open(caminho, 'a') as a: # senão, escreve no arquivo os dados informados. usando with para garantir que o arquivo seja fechado, e 'a' é de append.
            a.write(f'  - {nome} : {idade_inf} anos de idade\n')
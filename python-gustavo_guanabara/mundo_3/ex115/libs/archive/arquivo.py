import os

def arquivoexist(caminho):
    '''
    Função confere se o aqruivo já existe.
    param caminho: caminho onde o arquivo foi/deve ser criado.
    '''
    try:
        # se conseguir abrir e fechar o arquivo, retorna verdadeiro.
        a = open(caminho, 'r')
        a.close()
    except FileNotFoundError: # se ele não for localizado retorna falso.
        return False
    else:
        return True       

def criararquivo(caminho):
    '''
    Função para criação do arquivo. Só é executado caso a função 'arquivoexist' retorne False
    '''
    try:
        with open(caminho, 'a+') as a: # cria o arquivo com o parametro 'a+' que o cria automaticamente, e passa pois só precisa ser criado.
            pass
    except:
        print('\033[1;91mHouve um ERRO na criação do arquivo.\033[m') # caso algum erro tenha acontecido
    else:
        print('\033[1;91mArquivo criado com sucesso!\033[m')
    
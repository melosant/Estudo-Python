import os

def arquivoexist(caminho):
    try:
        a = open(caminho, 'r')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True       

def criararquivo(caminho):
    try:
        with open(caminho, 'a+') as a:
            pass
    except:
        print('\033[1;91mHouve um ERRO na criação do arquivo.\033[m')
    else:
        print('\033[1;91mArquivo criado com sucesso!\033[m')
    
# Pacote de módulos para interface.

from time import sleep

def mostrarMenu():
    '''
    Exibe menu interativo
    '''
    print('-' * 40)
    print('             MENU PRINCIPAL')
    print('-' * 40)
    print(f'''\033[1;93m1 -\033[m \033[1;34mVer Pessoas Cadastradas\033[m
\033[1;93m2 -\033[m \033[1;34mCadastrar Nova Pessoa\033[m
\033[1;93m3 -\033[m \033[1;34mSair do Sistema\033[m''')
    print('-' * 40)

def opc1():
    print('-' * 40)
    print('          PESSOAS CADASTRADAS')
    print('-' * 40)

def opc2():
    print('-' * 40)
    print('         CADASTRAR NOVA PESSOA')
    print('-' * 40)

def opc3():
    print('-' * 40)
    print('     Saindo do Sistema... Até Logo!')
    print('-' * 40)

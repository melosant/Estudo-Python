# importação de bibliotecas e módulos
from libs.interface.menu import *
from libs.archive.arquivo import *
from libs.functions.func_arch import *
from libs.functions.func_gerais import *
from time import sleep
import os

# fazendo a conexão para criação e alteração do arquivo txt
caminho_base = 'C:\\ESTUDO\\Estudo-Python\\python-gustavo_guanabara\\mundo_3\\ex115'
nome_arquivo = 'cadastro.txt'
caminho_completo = os.path.join(caminho_base, nome_arquivo)

# se o arquivo não existir, cria ele.
if not arquivoexist(caminho_completo):
    criararquivo(caminho_completo)
else:
    print('Arquivo já iniciado.')

# loop principal do programa
while True:
    mostrarMenu()

    # loop de entrada do usuário (com tratamento de erros de entradas.)
    while True:
        try:
            resp = int(input('\033[1;92mSua Opção:\033[m '))
            if resp > 3 or resp < 1:
                print('\033[1;91mDigite uma opção váida.\033[m') 
                continue
        except ValueError, TypeError:
            print('\033[1;91mDigite um número válido.\033[m')
        except KeyboardInterrupt:
            print('\033[1;91mCaso deseje parar o programa, selecione a opção 3.\033[m')
        else:
            break

    if resp == 1:
        opc1()
        opcaoum(caminho_completo) # ver pessoas cadastradas passando o caminho do arquivo
        continue
    elif resp == 2:
        opc2()
        opcaodois(caminho_completo) # cadastrar uma nova pessoa passando o caminho do arquivo
        continue
    else:
        opc3()
        break
sleep(1)
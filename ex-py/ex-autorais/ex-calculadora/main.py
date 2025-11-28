# proj calculadora bases de prog em py

# modulos e pacotes
from libs.func_input import *
from libs.func_output import *
from libs.interface import *

# bibliotecas padroes
from time import sleep

# loop principa
while True:
    # input de dados da compra
    exibirmenu('       \033[;1mLOJA ONLINE  ')
    nomeprod = leianome('\033[1;94mNome do Produto : \033[m')
    if nomeprod == None: # se interromper, break
        break
    code = leiacode('\033[1;94mCódigo do Produto : \033[m') 
    if code == None: # se interromper, break
        break
    precoprod = leiafloat('\033[1;94mPreço do Produto :\033[m \033[1;32mR$')
    if precoprod == None: # se interromper, break
        break
    pesoprod = leiafloat('\033[1;94mPeso do Produto (em kg): \033[m')
    if pesoprod == None: # se interromper, break
        break

    localentrega('  \033[;1mREGIÃO DA ENTREGA  ')

    opcao = leiaint('\033[1;95mSelecione Sua Região : \033[m')
    if opcao == None: # se interromper, break
        break
    elif opcao == 1:
        total, frete = opcaoum(precoprod, pesoprod)
        local = 'Região Sul'
    elif opcao == 2:
        total, frete = opcaodois(precoprod, pesoprod)
        local = 'Região Sudeste'
    elif opcao == 3:
        total, frete = opcaotres(precoprod, pesoprod)
        local = 'Região Norte'
    else:
        total, frete = opcaoquatro(precoprod, pesoprod)
        local = 'Região Nordeste'
 
    # pegando a data atual
    dataformatada, dataentrega = data_compra()

    resumo(nomeprod, code, precoprod, pesoprod, local, frete, total, dataformatada, dataentrega)
    break

sleep(1)
print('\n\033[;1mFim do Programa!')
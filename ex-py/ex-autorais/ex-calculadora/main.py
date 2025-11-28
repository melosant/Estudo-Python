# proj calculadora bases de prog

from libs.functions import *
import datetime
from time import sleep

while True:
    exibirmenu('       \033[;1mLOJA ONLINE  ')
    nomeprod = leianome('\033[1;94mNome do Produto : \033[m')
    if nomeprod == None:
        break
    code = leiacode('\033[1;94mCódigo do Produto : \033[m') 
    if code == None:
        break
    precoprod = leiafloat('\033[1;94mPreço do Produto :\033[m \033[1;32mR$')
    if precoprod == None:
        break
    pesoprod = leiafloat('\033[1;94mPeso do Produto (em kg): \033[m')
    if pesoprod == None:
        break

    localentrega('  \033[;1mREGIÃO DA ENTREGA  ')
    try:
        opcao = leiaint('\033[1;95mSelecione Sua Região : \033[m')
        if opcao == None:
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
    except KeyboardInterrupt:
        break

    data = datetime.date.today()
    dataf = datetime.date.strftime(data, '%d/%m/%Y')
    prazoentrega = 10
    prazo_delta = datetime.timedelta(days=prazoentrega)
    entrega = data + prazo_delta
    entrega = datetime.date.strftime(entrega, '%d/%m/%Y')

    resumo(nomeprod, code, precoprod, pesoprod, local, frete, total, dataf, entrega)
    break

sleep(1)
print('\n\033[;1mFim do Programa!')
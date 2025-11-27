from menu.interface import *
from time import sleep

while True:
    mostrarMenu()   

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
        continue
    elif resp == 2:
        opc2()
        continue
    else:
        opc3()
        break
sleep(1)
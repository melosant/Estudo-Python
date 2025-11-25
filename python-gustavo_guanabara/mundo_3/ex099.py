from time import sleep

def valores(*num):
    print()
    if len(num) == 0:
        print('Nenhum valor foi informado.')
        print('Não há maior valor informado.')
    else:
        for i in num:
            print(i, end=' ')
            sleep(0.2)
        print(f'Foram informados {len(num)} valores ao todo.')
        print(f'O maior valor informado foi {max(num)}')

valores(10, 8, 15, 3, 8, 9)
valores(4, 8, 9)
valores(6, 2)
valores(5)
valores()
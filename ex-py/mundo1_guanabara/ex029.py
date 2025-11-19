import math

km = float(input('Informe quantos km foram rodados : '))
if km <= 80.0:
    print('Tudo dentro das leis.')
else:
    diferenca = km - 80
    multa = math.trunc(diferenca) * 7.00
    print(f'Multado!! Valor a pagar : R${multa:.2f}')
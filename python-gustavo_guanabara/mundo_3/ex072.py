extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 
           'seis', 'sete', 'oito', 'nove', 'dez', 
           'onze', 'doze', 'treze', 'quatorze', 'quinze', 
           'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    while True:
        num = int(input('Digite um número entre 0-20 : '))
        if num < 0 or num > 20:
            print('Tente Novamente. ', end='')
        else:
            break
    break

print(f'Você digitou o número {extenso[num]}.')
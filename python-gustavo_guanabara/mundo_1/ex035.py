# programa 35 : verificação de existêncai de triângulos
# Condições if-else if-else (Aula 10)
# um lado nao pode ser maior q a soma dos outros 2

r1 = int(input('informe o valor da 1° reta : '))
r2 = int(input('informe o valor da 2° reta : '))
r3 = int(input('informe o valor da 3° reta : '))

if r1 + r2 < r3:
    print('NÃO PODE SER TRIÂNGULO!')
elif r2 + r3 < r1:
    print('NÃO PODE SER TRIÂNGULO!')
elif r1 + r3 < r2:
    print('NÃO PODE SER TRIÂNGULO!')
else:
    print('TRIÂNGULO FORMADO!')
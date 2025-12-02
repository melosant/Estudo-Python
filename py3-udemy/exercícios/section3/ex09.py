# Calculadora com while
# Aula 67-69

while True:
    while True:
        try: 
            n1 = float(input('Digite o primeiro número : '))
            n2 = float(input('Digite o segundo número : '))
            break
        except:
            print('Por favor, insira um número válido.')
    
    while True:
        op = input('Digite qual operador você deseja utilizar (+-/*): ')
        if op not in '+-/*':
            print('Digite um operador válido.')
        else:
            break

    if op == '+':
        print(f'{n1} + {n2} = {n1 + n2:.2f}')
    if op == '-':
        print(f'{n1} - {n2} = {n1 - n2:.2f}')
    if op == '/':
        print(f'{n1} / {n2} = {n1 / n2:.2f}')
    if op == '*':
        print(f'{n1} * {n2} = {n1 * n2:.2f}')

    resp = input('Deseja continuar [S/N] ? ').upper()
    if resp == 'N':
        break

print('FIM DA CALCULADORA.')
num = int(input('Informe o numero para conversão : '))
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('1 - Binário')
print('2 - Octal')
print('3 - Hexadecimal')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

opcao = int(input('Digite a opção desejada para conversão : '))
if opcao == 1:
    print(f'{num} em binário = {bin(num)[2:]}')
elif opcao == 2:
    print(f'{num} em octal = {oct(num)[2:]}')
elif opcao == 3:
    print(f'{num} em hexadecimal = {hex(num)[2:]}')
else:
    print('Opção não encontrada.')
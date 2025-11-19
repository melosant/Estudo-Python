from datetime import date

ano = int(input('Informe o ano de nascimento do jovem : '))
ano_atual = date.today().year

idade = ano_atual - ano

if idade <= 9:
    print(f'{idade} anos -> MIRIM')
elif idade <= 14:
    print(f'{idade} anos -> INFANTIL')
elif idade <= 19:
    print(f'{idade} anos -> JUNIOR')
elif idade <= 20:
    print(f'{idade} anos -> SENIOR')
else:
    print(f'{idade} anos -> MASTER.')
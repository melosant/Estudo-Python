from datetime import date

ano = int(input('Informe o ano de nascimento do jovem : '))
ano_atual = date.today().year

idade = ano_atual - ano

if idade > 18:
    print(f'Já passou do prazo do alistamento. Atrasado {idade - 18} ano(s).')
elif idade < 18:
    print(f'Ainda não está na idade de se alistar. Faltam {18 - idade} ano(s).')
else:
    print('Está na idade de se alistar!!')
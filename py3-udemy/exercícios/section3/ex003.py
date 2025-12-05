# Comparação de strings
# Aula 39

primeiro_valor = input('Digite o primeiro valor : ')
segundo_valor = input('Digite o segundo valor : ')

if primeiro_valor > segundo_valor:
    print(f'O {primeiro_valor=} é maior do que o {segundo_valor=}')
elif segundo_valor > primeiro_valor:
    print(f'O {segundo_valor=} é maior do que o {primeiro_valor=}')
else:
    print(f'Os valores {primeiro_valor=} e {segundo_valor=} são iguais.')
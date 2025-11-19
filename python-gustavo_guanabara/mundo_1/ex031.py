km = int(input('Informe a distância da viagem (em km) : '))
if km <= 200:
    passagem = km * 0.50
else:
    passagem = km * 0.45

print(f'O valor da passagem é de R${passagem}')
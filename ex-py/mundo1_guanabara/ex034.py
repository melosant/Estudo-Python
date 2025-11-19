salario = float(input('Informe o salário do funcionário : R$'))
if salario > 1250:
    aumento = salario * 1.10
else:
    aumento = salario * 1.15

print(f'NOVO SALÁRIO APÓS AUMENTO = R${aumento}')
dias = int(input('Quantos dias o carro foi alugado ? '))
km = float(input('Informe quantos km rodados : '))

tax_dias = 60 * dias
tax_km = 0.15 * km
tax_total = tax_dias + tax_km

print(f'O total a pagar é de R${tax_total:.2f}')
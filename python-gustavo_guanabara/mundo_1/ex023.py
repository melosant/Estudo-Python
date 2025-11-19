num = int(input('Informe o número (0-9999) : '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(f'''
NÚMERO : {num}

UNIDADE : {u}
DEZENA : {d}
CENTENA : {c}
MILHAR : {m}''')
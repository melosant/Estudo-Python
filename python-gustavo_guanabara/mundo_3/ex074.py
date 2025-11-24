import random
tupla = (random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10))

print(f'''
Números Sorteados : {tupla}
Maior número : {max(tupla)}
Menor Número : {min(tupla)}''')
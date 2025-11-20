num = int(input("Digite um numero : "))
fatorial = 1
num_temporario = num

while num_temporario != 0:
    fatorial *= num_temporario
    num_temporario -= 1

print(f'{num}! = {fatorial}')
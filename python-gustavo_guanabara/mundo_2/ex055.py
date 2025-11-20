peso = float(input('Digite um peso (kg) : '))
maior = peso
menor = peso

for i in range(4):
    peso = float(input('Digite um peso (kg) : '))
    if peso > maior :
        maior = peso
    elif peso < menor:
        menor = peso

print(f'O maior peso foi {maior} e o menor {menor}.')
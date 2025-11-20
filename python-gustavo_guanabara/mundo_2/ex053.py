frase = input('Digite uma frase/palavra : ').strip().upper()
palavras = frase.split()
junto = ''.join(palavras) # junta as palavras dps de separá-las no split
inverso = ''

for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]

if inverso == junto:
    print(f'{frase} - É um palíndromo.')
else:
    print(f'{frase} - Não é um palíndromo.')

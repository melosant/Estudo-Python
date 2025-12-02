# Iterando uma frase e descorindo qual letra apareceu mais vezes
# Aula 71

frase = 'aaaooooooooooaaaiiiiiiiiiiiiiiipppppppppp'.upper()

i = 0
qtd_letra = 0
letra_mais = ''

while i < len(frase):
    letra_atual = frase[i]
    
    if letra_atual == ' ':
        i += 1
        continue

    qtd_letra_atual = frase.count(letra_atual)

    if qtd_letra_atual > qtd_letra:
        qtd_letra = qtd_letra_atual
        letra_mais = letra_atual

    i += 1

print(f'A letra que mais apareceu foi {letra_mais}, aparecendo {qtd_letra} vezes.')
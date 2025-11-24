palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 
         'PYTHON', 'CURSO', 'GRATIS',
         'ESTUDAR', 'PRATICAR', 'TRABALHAR', 
         'MERCADO', 'PROGRAMADOR', 'FUTURO')

for pal in palavras:
    print(f'\nNa palavra {pal} temos ', end='')
    for letter in pal:
        if letter.upper() in 'AEIOU':
            print(letter, end=' ')
frase = input('Digite uma frase : ').upper().strip()

print(f'''
QUANTAS VEZES APARECE "A" : {frase.count('A')}
EM QUE POSIÇÃO APARECE A PRIMEIRA : {frase.find('A')+ 1}
EM QUE POSIÇÃO APARECE A ÚLTIMA : {frase.rfind('A')+ 1}
''')
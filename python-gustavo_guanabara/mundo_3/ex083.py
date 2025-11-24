expr = str(input('Digite um expressão matemática: '))
pilha = []

for simb in expr:
    if simb == '(':
        pilha.append('(')
    else:
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('Sua expressão é válida.')
else:
    print('Sua expressão está errada,')
    
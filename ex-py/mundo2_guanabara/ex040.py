n1 = float(input('Informe a primeira nota do aluno : '))
n2 = float(input('Informe a segunda nota do aluno : '))

media = (n1 + n2) / 2

if media >= 7.0:
    print(f'MÉDIA : {media:.2f}. APROVADO.')
elif media >= 5.0 and media <= 6.9:
    print(f'MÉDIA : {media:.2f}. RECUPERAÇÃO.')
else:
    print(f'MÉDIA : {media:.2f}. REPROVADO.')
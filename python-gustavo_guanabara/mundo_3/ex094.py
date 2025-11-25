pessoas_geral = list()
pessoa = dict()
media = 0

while True:
    print()
    print('-' * 20)
    pessoa['Nome'] = str(input('Nome : ').capitalize())
    pessoa['Sexo'] = str(input('Sexo [M/F] : ').upper())
    pessoa['Idade'] = int(input('Idade : '))
    media += pessoa['Idade']

    pessoas_geral.append(pessoa.copy())

    resp = input('Deseja cadastrar outra pessoa [S/N] ? ').upper()
    if resp =='N':
        break

media = media / len(pessoas_geral)
print('-=' * 40)
print(f'- O total de pessoas cadastradas foi {len(pessoas_geral)}.')
print(f'- A média de idade é de {media:.2f}')
print(f'- As mulheres cadastradas foram ', end='')
for p in pessoas_geral:
    if p['Sexo'] == 'F':
        print(f'{p['Nome']}', end=' ')

print(f'\n- A lista de pessoas que estão acima da média:')
for p in pessoas_geral:
    if p['Idade'] > media:
        for k,v in p.items():
            print(f'    => {k} = {v}; ', end='')
    print()

print('\nFIM DO PROGRAMA!')
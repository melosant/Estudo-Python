jogador = {}
gols = list()
soma = 0

jogador['Nome'] = str(input('Nome do Jogador : ').capitalize())
qtd = int(input(f'Quantas partidas {jogador["Nome"]} jogou ? '))

for i in range(qtd):
    qtdgols = int(input(f'Quantos gols na partida {i+1} : '))
    gols.append(qtdgols)
    soma += qtdgols

jogador['Gols'] = gols
jogador['TotalGols'] = soma

print('-=' * 40)
print(jogador)
print('-=' * 40)
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}')
print('-=' * 40)
print(f'O jogador {jogador['Nome']} jogou {qtd} partidas.')
for i in range(qtd):
    print(f'    => Na Partida {i+1}, fez {jogador["Gols"][i]}')
print(f'Foi um total de {jogador["TotalGols"]} gols.')
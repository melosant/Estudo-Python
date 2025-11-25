# aprimoramento do ex 093
jogadores = list()
jogador = dict()
gols = list()

while True:
    soma = 0
    jogador['Nome'] = str(input('Nome do Jogador : ').capitalize())
    qtd = int(input(f'Quantas partidas {jogador["Nome"]} jogou ? '))

    for i in range(qtd):
        qtdgols = int(input(f'Quantos gols na partida {i+1} : '))
        gols.append(qtdgols)
        soma += qtdgols

    jogador['Gols'] = gols[:]
    jogador['TotalGols'] = soma
    jogadores.append(jogador.copy())

    gols.clear()

    resp = input('Deseja registrar outro [S/N] ? ').upper()
    if resp == 'N':
        break

print()
print('-=' * 20)
print()
for i, jog in enumerate(jogadores):
    print(i, end='    ')
    print(f'{jog["Nome"]}', end='     ')
    print(f'{jog["Gols"]}', end='     ')
    print(f'{jog["TotalGols"]}')

while True:
    opc = int(input('\nMostrar detalhamento de qual jogador (No. / 999 para parar) : '))
    if opc == 999:
        break
    elif opc >= 0 and opc <= len(jogadores):
        print()
        for jog in jogadores:
            if opc == jogadores.index(jog):
                print(f'DETALHAMENTO JOGADOR {jog["Nome"]}')
                for i in range(qtd):
                    print(f'    => Na Partida {i+1}, fez {jog["Gols"][i]}')
                continue
    else:
        print(f'Não existe jogador {opc}. Digite uma opção válida. ', end='')

print('\nFim do programa!')
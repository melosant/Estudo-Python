from random import randint

wins = 0

while True:
    print('''
=-=-=-=-=-=-=-=-=-=-=-=-
VAMOS JOGAR PAR OU ÍMPAR
-=-=-=-=-=-=-=-=-=-=-=-=\n''')
    n = int(input('Digite um valor (0-10) : '))
    escolha = input('Par ou Ímpar ? [P/I] ').upper()
    npc = randint(0, 10)
    total = n + npc

    if total % 2 == 0:
        if escolha == 'P':
            print('\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n')
            print(f'Você jogou {n} e o computador jogou {npc}. Total de {total} deu PAR!')
            print('Você venceu!')
            wins += 1
        else:
            print('\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n')
            print(f'Você jogou {n} e o computador jogou {npc}. Total de {total} deu PAR!')
            print('Você perdeu!')
            break
    else:
        if escolha == 'I':
            print('\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n')
            print(f'Você jogou {n} e o computador jogou {npc}. Total de {total} deu ÍMPAR!')
            print('Você venceu!')
            wins += 1
        else:
            print(f'Você jogou {n} e o computador jogou {npc}. Total de {total} deu ÍMPAR!')
            print('Você perdeu.')
            break

print('\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n')
print(f'Fim de Jogo. Você venceu {wins} vezes.\n')
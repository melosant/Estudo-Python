tabela = ('FLamengo', 'Palmeiras', 'Cruzeiro', 'Mirassol', 
          'Botafogo', 'Bahia', 'Fluminense', 'São Paulo', 
          'RB Bragantino', 'Corinthians', 'Atlético MG', 'Grêmio', 
          'Vasco', 'Ceará', 'Internacional', 'Vitória', 
          'Santos', 'Fortaleza', 'Juventude', 'Sport')

print('=-' * 30)
print(f'Classificação de momento : {tabela}')
print('=-' * 30)
print(f'G4 : {tabela[0:4]}')
print('=-' * 30)
print(f'Z4 : {tabela[-4:]}')
print('=-' * 30)
print(f'Ordem Alfabética : {sorted(tabela)}')
print('=-' * 30)
print(f'O RB Bragantino está na {tabela.index('RB Bragantino') + 1}° posição.')
print('=-' * 30)
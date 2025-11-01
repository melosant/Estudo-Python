# Programa 22 - Simulador de Dados
import random # biblioteca para gerar dados aleatoriamente
import time # biblioteca para manipulação do tempo da saída de dados

dado1 = random.randint(1, 6) # será gerado um valor aleatório no intervalo (1,6)
dado2 = random.randint(1, 6) # será gerado um valor aleatório no intervalo (1,6)

print("Lançando dados...")
time.sleep(1.0) # 1 segundo de intervalo até a próxima saída
print(f"\nDado 1 : {dado1}")
time.sleep(1.0) # 1 segundo de intervalo até a próxima saída
print(f"\nDado 2 : {dado2}")
time.sleep(0.5) # 0.5 segundos de intervalo até a próxima saída
# resultado combinado da rolagem dos dados 
print(f"\nResultado : ", dado1 + dado2)
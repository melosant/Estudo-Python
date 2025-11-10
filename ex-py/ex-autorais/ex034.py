# Programa 34 - Controle de Caixa Simples
import time
import os

saldo_total = 0.0

def exibirmenu():
    time.sleep(2.0)
    os.system("cls")

    print("=" * 13)
    print("  MELO BANK")
    print("=" * 13)
    print(f"\nSALDO ATUAL : R${saldo_total}")

    print("""\n
SELECIONE SUA OPÇÃO:
1 - DEPOSITAR
2 - SAQUE
3 - SAIR""")
    
def depositar():
    global saldo_total
    deposito = float(input("\nDIGITE O VALOR DO DEPÓSITO : R$"))
    saldo_total += deposito

def sacar():
    global saldo_total
    print(f"\nSALDO ATUAL : R${saldo_total}")
    retirada = float(input(f"\nDIGITE O VALOR PARA SAQUE : R$"))
    if retirada > saldo_total:
        print("\nDIGITE UM VALOR VÁLIDO PARA SAQUE!")
    else:
        saldo_total -= retirada 

def finalizacao():
    print("\nSaindo...")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print(".")
    print("Programa Finalizado!")

while True:
    exibirmenu()
    opcao = int(input("(1-3): "))

    if opcao == 1:
        depositar()
    elif opcao == 2:
        sacar()
    elif opcao == 3:
        break
    else:
        print("\nDIGITE UMA OPÇÃO VÁLIDA!")

finalizacao()
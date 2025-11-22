while True:
    valor = int(input('Digite o valor que deseja sacar : R$'))
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    
    notas50 = valor // 50
    resto = valor % 50
    print(f'Total de cédulas de R$50 : {notas50}.')
    if resto == 0:
        break

    notas20 = resto // 20
    resto = resto % 20
    print(f'Total de cédulas de R$20 : {notas20}.')
    if resto == 0:
        break
    
    notas10 = resto // 10
    resto = resto % 10
    print(f'Total de cédulas de R$10 : {notas10}.')
    if resto == 0:
        break
    
    notas1 = resto // 1
    print(f'Total de cédulas de R$1 : {notas1}.')
    break
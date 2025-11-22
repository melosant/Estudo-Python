qtd18 = qtdh = qtdm = 0

while True:
    print('''
-------------------------------
     CADASTRO DE PESSOAS
-------------------------------''')

    idade = int(input('Idade : '))
    if idade > 18:
        qtd18 += 1
    while True:
        sexo = input("Sexo [M/F] : ").upper()
        if sexo == 'M' or sexo == 'F':
            if sexo == 'M':
                qtdh += 1
            else:
                if idade < 20:
                    qtdm += 1
            break
    
    while True:
        controle = input('Deseja continuar [S/N] ? ').upper()
        if controle == 'S' or controle == 'N':
            break

    if controle == 'N':
        break

print(f'''
------------------------------------
          FIM DO PROGRAMA
Total de pessoas com mais de 18 anos : {qtd18}
Ao todo temos {qtdh} homens cadastrados.
E temos {qtdm} mulheres cadastradas com menos de 20 anos.\n
''')
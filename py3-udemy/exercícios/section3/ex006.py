# Saudação de acordo com o horário
# Aula 55

try:
    hora = int(input('Digite a hora atual (h): '))
    if hora >= 0 and hora < 12:
        print('Bom dia!')
    elif hora >= 12 and hora < 18:
        print('Boa Tarde!')
    elif hora >= 18 and hora <= 23:
        print('Boa Noite!')
    else:
        print('Hora não válida.')
except:
    print('Hora digitada não válida.')
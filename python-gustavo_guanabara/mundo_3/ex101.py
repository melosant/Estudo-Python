# Programa 101 : verificação idade para votar
# Funções / Escopo de Variáveis (Aula 21)

def voto(ano):
    from datetime import date
    anoatual = date.today().year
    ano = anoatual - ano
    if ano < 18:
        return 'NÃO VOTA'
    elif ano >= 18 and ano < 65:
        return 'VOTO OBRIGATÓRIO'
    else:
        return 'VOTO OPCIONAL'

print('-' * 40)
anonasc = int(input('Digite o ano em que você nasceu : '))
resp = voto(anonasc)
print(f'Com {2025 - anonasc} anos : {resp}!')
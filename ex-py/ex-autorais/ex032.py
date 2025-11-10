# Programa 32 - Ano Bissexto + Dias no Mês

# função do programa 31
def ano_bissexto(ano):
    if ano % 4 == 0 and ano % 100 != 0:
        return "ano bissexto"
    if ano % 400 == 0:
        return "ano bissexto"
    else:
        return "ano não bissexto."
    
# função dos dias do mes
def dias_mes(ano, mes):
    dias = [31,28,31,30,31,30,31,31,30,31,30,31]
    result = dias[mes-1] # usuário responde, e vai puxar indice na lista de acordo com a resposta -1.
    if mes > 12:
        return None
    elif mes == 2 and ano_bissexto(ano): # se for fevereiro e ano bissexto, tem 29 dias.
        result = 29
    return result

while True:
    resp_ano = int(input("Digite um ano (digite 0 para parar) : "))
    resp_mes = int(input("Selecione um mês (1-12 / 0 para o loop) : "))
    if resp_ano == 0 or resp_mes == 0: 
        break
    else:
        print(f"{resp_ano} -> {ano_bissexto(resp_ano)}")
        print(f"{resp_mes} -> {dias_mes(resp_ano, resp_mes)}")

print("\nPrograma finalizado!")
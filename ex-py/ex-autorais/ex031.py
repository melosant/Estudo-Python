# Programa 31 - Ano Bissexto 

# se divisível por 4 e não divisível por 100 é bissexto
# senao, se for divisível por 400 é bissexto
# caso contrário, não é um ano bissexto
def ano_bissexto(ano):
    if ano % 4 == 0 and ano % 100 != 0:
        return "ano bissexto"
    if ano % 400 == 0:
        return "ano bissexto"
    else:
        return "ano não bissexto."

while True:
    resp_ano = int(input("Digite um ano (digite 0 para parar) : "))
    if resp_ano == 0 : 
        break
    else:
        print(f"{resp_ano} -> {ano_bissexto(resp_ano)}") # chamada da função

print("\nPrograma finalizado!")
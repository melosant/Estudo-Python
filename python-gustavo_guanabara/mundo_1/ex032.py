from datetime import date

ano = int(input('Informe um ano para conferência. Coloque 0 para analisar o ano atual (yyyy): '))

if ano == 0:
    ano = date.today().year
if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print(f'{ano} -> BISSEXTO')
        else:
            print(f"{ano} -> NÂO É BISSEXTO")
    else:
        print(f'{ano} -> BISSEXTO')
else:
    print(f"{ano} -> NÂO É BISSEXTO")
def metade(price, form=False):
    metade = price / 2
    if form==True:
        return moeda(metade)
    else:
        return metade

def dobro(price, form=False):
    dobrar = price * 2
    if form==True:
        return moeda(dobrar)
    else:
        return dobrar

def aumentar(price, a, form=False):
    aumento = price + (price * a/100)
    if form==True:
        return moeda(aumento)
    else:
        return aumento

def diminuir(price, d, form=False):
    reduzir = price - (price * d/100)
    if form==True:
        return moeda(reduzir)
    else:
        return reduzir
    
def resumo(price, a, d):
    print(f'''
------------------------------
      RESUMO DO VALOR
------------------------------
A metade de {moeda(price)} é {metade(price, True)}.
O dobro de {moeda(price)} é {dobro(price, True)}.
Aumentando {a}% em {moeda(price)} fica {aumentar(price, a, True)}
Diminuindo {d}% em {moeda(price)} fica {diminuir(price, d, True)}
------------------------------\n''')

def moeda(p):
    return f'R${p:.2f}'
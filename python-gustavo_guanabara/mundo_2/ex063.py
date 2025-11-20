n = int(input('Quantos termos da sequência você quer ver ? '))
cont = 0
t1 = 1
t2 = 1
t3 = 0

print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('   SEQUÊNCIA DE FIBONACCI')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

print('0', end=' ')
while cont < (n - 1):
    print(t1, end=' ')
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    cont += 1
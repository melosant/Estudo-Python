# mesmo codigo do ex009, pois já tinha feito assim
num = int(input('Digite um número para ver a tabuada : '))

# no curso foi feito um a um, utilizei loop for
print('=' * 20)
for i in range(11):
    print(f'{num} x {i} = {num * i}')
    i += 1
print('=' * 20)
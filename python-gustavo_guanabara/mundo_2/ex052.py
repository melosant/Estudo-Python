num = int(input('Digite o número para verificação : '))
verif = False

if num == 2 or num == 1:
    print(f'{num} -> PRIMO')
else:
    for i in range(2, num):
        if num % i == 0:
            verif = False
            break
        else:
            verif = True

    if verif == True:
        print(f'{num} -> PRIMO')
    else:
        print(f'{num} -> NÃO PRIMO')
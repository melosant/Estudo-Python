while True:
    n = int(input(f'''
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Quer ver a tabuada de qual valor ? 
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n'''))
    print()
    if n < 0:
        break
    else:
        for i in range(11):
            print(f'{n} x {i} = {n * i}')

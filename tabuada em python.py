cont = 1
n = 0
while n >= 0:
    print('-' * 40)
    n = int(input('Quer ver a tabuada de que número? '))
    while cont < 12:
        if n < 0:
            print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
            break
        tab = n * cont
        print(f'{n} x {cont} = {tab}')
        cont += 1
        if cont == 11:
            cont = 0
            break

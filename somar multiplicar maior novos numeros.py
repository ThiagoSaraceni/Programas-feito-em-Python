from time import sleep
maior = 0
resp = 0
n1 = int(input('\033[1mDigite o primeiro valor: '))
n2 = int(input('\033[1mDigite o segundo valor: '))
soma = n1 + n2
mult = n1*n2
while resp != 5:
    print('\033[1;31mMENU')
    print('\033[1;35m[1] SOMAR')
    print('\033[1;35m[2] MULTIPLICAR')
    print('\033[1;35m[3] MAIOR')
    print('\033[1;35m[4] NOVOS NÚMEROS: ')
    print('\033[1;35m[5] SAIR DO PROGRAMA')
    resp = int(input('\n\33[mQual opção vai escolher do menu? '))
    if resp == 1:
        print('A soma entre {} + {} vai ser {} '.format(n1, n2, soma))
    if resp == 2:
        print('A multilicação entre {} x {} é {}'.format(n1, n2, mult))
    if resp == 3:
        maior = n1
        if n2 > maior:
            maior = n2
        if n1 == n2:
            print('Os números são iguais.')
        print('O maior número é {}'.format(maior))
    if resp == 4:
        maior = 0
        resp = 0
        n1 = int(input('\033[1mDigite o primeiro valor: '))
        n2 = int(input('\033[1mDigite o segundo valor: '))
        soma = n1 + n2
        mult = n1 * n2
        print('\033[1;31mMENU')
        print('\033[1;35m[1] SOMAR')
        print('\033[1;35m[2] MULTIPLICAR')
        print('\033[1;35m[3] MAIOR')
        print('\033[1;35m[4] NOVOS NÚMEROS: ')
        print('\033[1;35m[5] SAIR DO PROGRAMA')
        #OU PODERIA APENAS FAZER
        #n1 = int(input('Primeiro valor: '))
        #n2 = int(input('Segundo valor: '))

    if resp == 5:
        print('Finalizando...')
    if resp != 1 and resp != 2 and resp != 3 and resp != 4 and resp !=5:
        print('OPCAO INVALIDA. TENTE NOVAMENTE')
    sleep(2)
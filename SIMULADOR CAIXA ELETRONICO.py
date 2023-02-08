resto = celulas = 0
print('='*30)
print('{:^30}'.format('SIMULADOR DE CAIXA ELETRONICO.'))
print('='*30)
n = int(input('Qual valor você quer sacar?'))
if n // 50 != 0:
    celulas = n // 50
    n = n % 50
    print('Total de {} células de 50R$'.format(celulas))
if n // 20 != 0:
    celulas = n // 20
    print('Total de {} células de 20R$'.format(celulas))
    n = n % 20
if n // 10 != 0:
    celulas = n // 10
    print(f'Total de {celulas} células de 10R$')
    n = n % 10
if n // 1 != 0:
    celulas = n // 1
    print(f'Total de {celulas} células de 1R$')
print('='*30)
print('Volte sempre ao BANCO CURSO EM VÍDEO! Tenha um Bom dia!')

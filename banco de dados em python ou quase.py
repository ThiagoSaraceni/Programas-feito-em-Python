mulhermenorvinte = 0
maioridade = 0
maior = 0
nomehomem = str('')
media = 0
masculino = 0
feminino = 0
for c in range(1,5):
    print('---- {}ª PESSOA -----'.format(c))
    nome = str(input('Digite o {}° nome: '.format(c))).strip()
    idade = int(input('Digite a idade da {}ª pessoa: '.format(c)))
    sexo = str(input('Qual o sexo da {}ª pessoa? [M/F]: '.format(c))).capitalize().strip()
    media = media + idade
    if sexo in 'Mm':
        masculino = masculino + 1
        if idade > maioridade:
            maioridade = idade
            nomehomem = nome
    elif sexo == 'F':
        feminino = feminino + 1
        if idade < 20:
            mulhermenorvinte = mulhermenorvinte + 1
mediage = media/4
print('tem {} mulheres'.format(feminino))
print('tem {} homens'.format(masculino))
print('A média de idade do grupo é {}'.format(mediage))
print('O nome do homem mais velho tem {} anos e se chama {}'.format(maioridade ,nomehomem))
print('Tem {} mulheres com menos de 20 anos'.format(mulhermenorvinte))
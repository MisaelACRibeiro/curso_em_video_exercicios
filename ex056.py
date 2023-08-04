'''Desenvolva um programa que leia o NOME, IDADE E SEXO de 4 pessoas.
No final do programa, mostre:
►A média de idade do grupo
►Qual é o nome do Homem mais VELHO
►Quantas mulheres têm menos de 20 anos.'''
somaidade =
media = 0
hmv = 0
contmu = 0
for i in range(1, 5):
    print('------ {}° Pessoa -------'.format(i))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    items = ('Homem', 'Mulher')
    sexo = int(input('Digite [0]Homem [1]Mulher: '))
    somaidade += idade
    if sexo == 0:
        if i == 1:
            hmv = idade
        else:
            if idade > hmv:
                hmv = idade
    else:
        if idade < 20:
            contmu += 1
media = somaidade / 4
print('O nome do homem mais velho é {}'.format(nome))
print('A média da idade do grupo é {}'.format(media))
print('{} mulheres tem menos de 20 anos'.format(contmu))
print('{}, {}, {},'.format(nome, idade, items[sexo]))

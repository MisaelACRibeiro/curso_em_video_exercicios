'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar.
no final, mostre:
A) Qual é o total gasto no compra.
B) Quantos produtos custam mais de RS 1.000,00
C) Qual é o nome do produto mais barato'''

total = caro = vb = menor = 0
barato = ' '
while True:
    prod = str(input('Informe o nome do produto: '))
    valor = float(input('Qual é o valor? R$ '))
    total += valor
    vb += 1
    if valor > 1000:
        caro += 1
    if vb == 1 or valor < menor:
        barato = prod
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if cont == 'N':
        break
print(f'Sua compra ficou em R$ {total:.2f}')
print(f'Tem {caro} que custa mais de R$ 1.000,00')
print(f'O produto mais barato é o {barato}')

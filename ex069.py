'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
o programa deverá perguntar se o usuário quer ou não continuar. No final mostre:
A) Quantas pessoas tem mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres tem menos de 20 anos.'''
contIdade = contSexo = Fmais = 0
while True:
    print('-'*30)
    print('Cadastre uma pessoa')
    print('-'*30)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if idade >= 18:
            contIdade += 1
        if sexo == 'M':
            contSexo += 1
        elif sexo == 'F': #outro jeito : if sexo == 'F' and idade < 20:
            if idade <= 20:
                Fmais += 1
    opção = ' '
    while opção not in 'SN':
        opção = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if opção == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {contIdade}')
print(f'Ao todo temos {contSexo} homens cadastrados')
print(f'e temos {Fmais} mulheres com menos de 20 anos')

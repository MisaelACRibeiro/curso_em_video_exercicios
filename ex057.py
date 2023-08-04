'''Faça um programa que leia o SEXO de uma pessoa, mas só aceite os valores 'M' ou 'F'.
Caso esteja errado peça a digitação novamente até ter um valor correto.'''
sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Informe apenas [MF]: ')).strip().upper()[0]
print('OK sexo {} cadastrado'.format(sexo))

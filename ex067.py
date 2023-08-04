'''Faça um programa que mostre a tabuada de vários números, um de vada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.'''
while True:
    num = int(input('Digite um número para ver sua Tabuada: '))
    if num > 0:
        for c in range(1, 11):
            print(f'{num} X {c:2} = {c*num}')
    elif num < 0:
        break
print('fim')

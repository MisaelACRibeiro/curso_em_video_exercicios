'''Crie um programa que leia vários númeroa inteiros pelo teclado.
O program só vai para quando o usuário digitar o valos 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual a soma entre eles(desconsiderando o flag).'''

n = 0
soma = 0
cont = 0
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    cont += 1
    if n != 999:
        soma += n
print('Você digitou {} número e a soma entre eles foi {}.'.format(cont - 1, soma))

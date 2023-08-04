'''Faça um programa que jogue par ou impar com o computado. O jogo só srá interompido quando o jogador perder,
mostrando o total de vitorias consecutivas que ele conquistou no final do jogo.'''
from random import randint
jogada = 0
vitoria = 0
print('Jogando Par ou Impar')
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    soma = computador + jogador
    opção = ' '
    while opção not in 'PI':
        opção = str(input('Par ou Impar? [ P / I ] ').upper())[0]
    if opção == 'P':
        jogada += 1
        if soma % 2 == 0:
            print('Venceu!')
            vitoria += 1
            print(f'computador jogou {computador}')
        else:
            print('Perdeu!')
            print(f'computador jogou {computador}')
            break
    elif opção == 'I':
        jogada += 1
        if soma % 2 != 0:
            print('Venceu!')
            vitoria += 1
            print(f'Computador jogou {computador}')
        else:
            print('Perdeu!')
            print(f'computador jogou {computador}')
            break
print(f'Resultado: Você ganhou {vitoria} vezes, no total de {jogada} jogadas')
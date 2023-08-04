from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
maq = randint(0, 2)
print('''Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
print('Maquina jogou {}'.format(itens[maq]))
print('Você jogou {}'.format(itens[jogador]))
if maq == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('Maquina Vence!')
    elif jogador == 2:
        print('Jogador Vence!')
    else:
        print('Opção invalida')
elif maq == 1:
    if jogador == 0:
        print('Jogador Vence!')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('Maquina Vence!')
    else:
        print('Opção invalida')
elif maq == 2:
    if jogador == 0:
        print('Jogador Vence!')
    elif jogador == 1:
        print('Maquina Vence!')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('Opção invalida')

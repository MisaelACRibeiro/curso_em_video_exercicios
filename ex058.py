'''Melhore o jogo do DESAFIO 028 onde o computados vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar advinhar até acertar,
mostrando no final quantos palpites foram necessários para vencer.'''
import random
print('Adivinhe qual numero o PC escolheu')
pc = 0
liata = range(1, 11)
n = random.choice(liata)
jogador = int(input('Digite um número entre 1 e 10: '))
while n != jogador:
    if n > jogador:
        print('Mais ↑ tente outra vez.')
        jogador = int(input('Qual é seu palpite? '))
        pc += 1
    elif n < jogador:
        print('Menos ↓ tente outra vez.')
        jogador = int(input('Qual é seu palpite? '))
        pc +=1
print('GANHOU!')
print('você jogou {} vezes para acertar '.format(pc))

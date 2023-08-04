import random
print('{:=^40}'.format(' JOKENPÔ '))
print('Faça a sua jogada!')
escolha = int(input('''[1] Pedra
[2] Papel
[3] Tesoura
Escolha com sabedoria: '''))
lista = [1, 2, 3]
maq = random.choice(lista)
print('Você escolheu {} e a maquina escolheu {}'.format(escolha, maq))
if escolha == maq:
    print('Empate')
elif escolha == 1 and maq == 2 or escolha == 2 and maq == 3 or escolha == 3 and maq == 1:
    print('A Maquina Venceu!')
else:
    print('Você GANHOU!')

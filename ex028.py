import random

print('Adivinhe o mumero escolido')
lista = [0, 1, 2, 3, 4, 5]
escolido = int(input('Digite um numero de 0 á 5: '))
n = random.choice(lista)
if escolido == n:
    print('Acertou o numero escolido foi {}'. format(n))
else:
    print('Errou o numero escolido foi {}'.format(n))

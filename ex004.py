'''from math import trunc
num = float(input('Digite um número: '))
print('O valor digitado é {} e a porção inteira é {}'.format(num, trunc(num)))
import math
ang = float(input('Digite um angulo: '))
n = math.radians(ang)
print('O valor do seno é {:.2f}\nO valor do cosseno é {:.2f}\nO valor da tangente é {:.2f}'.format(math.cos(n),
math.sin(n), math.tan(n)))
import random
n1 = str(input('Digite o primeiro nome: '))
n2 = str(input('Digite o segundo nome: '))
n3 = str(input('Digite o terceiro nome: '))
n4 = str(input('Digite o quarto nome: '))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O escolhido foi {}'.format(escolhido))'''
import random
n1 = str(input('Digite o primeiro nome: '))
n2 = str(input('Digite o segundo nome: '))
n3 = str(input('Digite o terceiro nome: '))
n4 = str(input('Digite o quarto nome: '))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A ordem é: ')
print(lista)

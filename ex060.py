'''Faça um programa que leia um número qualquer e mostre o seu fatorial
5! = 5x4x3x2x1 = 120'''

'''from math import factorial
n = int(input('Digite um número para saber seu fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}'.format(n, f))

n = int(input('Calcular o Fatorial: '))
c = n
f = 1
while c > 0:
    print('{}'.format(c), end='')
    print(' X ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f)'''

n = int(input('Calcular o fatorial: '))
f = 1
c = n
for c in range(1, n+1):
    f *= c
    print(f)
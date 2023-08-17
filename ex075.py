'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes aparece o valor 9.
B)Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.'''

num = (int(input('Digite o primeiro número: ')),
       int(input('Digite o segundo número: ')),
       int(input('Digite o terceiro número: ')),
       int(input('Digite o quarto número: ')))
print(f'Os números digitados foram {num}')
print(f'O número 9 aparece {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado')
print('Os valores pares digitados foram ', end='')
for i in num:
    if i % 2 == 0:
        print(i, end=' ')
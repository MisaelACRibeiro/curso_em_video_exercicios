print('{:*^40}'.format(' Tabuada '))
numero = int(input('Digite um número: '))
cont = 0
for i in range(1, 11):
    cont += 1
    i = numero * cont
    print('{} x {:2} = {}'.format(numero, cont, i))
print('fim')


# ou esse jeito
num = int(input('Digite um numero para ver su tabuada: '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, num*c))

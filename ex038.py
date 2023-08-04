print('Analise de numero')
n1 = int(input('Digite um numero inteiro: '))
n2 = int(input('Digite outro numero inteiro: '))
if n1 > n2:
    print('O primeiro numero {} é maior que {}'.format(n1, n2))
elif n1 < n2:
    print('O segundo numero {} é maior que {}'.format(n2, n1))
else:
    print('{} e {} são iquais'.format(n1, n2))

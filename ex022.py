num = int(input('Informe um número entre 0 á 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}'.format(num))
if u != 0:
    print('Unidade: {}'.format(u))
if d != 0:
    print('Dezena: {}'.format(d))
if c != 0:
    print('Centena: {}'.format(c))
if m != 0:
    print('Milhar: {}'.format(m))

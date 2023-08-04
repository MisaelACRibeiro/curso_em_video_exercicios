print('Somando números pares')
resut = 0
for i in range(1, 7):
    soma = int(input('Digite o {} valor: '.format(i)))
    if soma % 2 == 0:
        resut += soma
print('A soma dos números pares é {}'.format(resut))

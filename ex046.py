'''rows = 8
for i in range(1, rows):
    for j in range(1, rows - i):
        print(' ', end='')
    for j in range(0, 2 * i - 1):
        print('*', end='')
    print()'''

from time import sleep
for c in range(10, 0, -1):# ou pode ser range(10, -1, -1) para ir até o numero 0
    print(c)
    sleep(0.5)
print('Feliz Ano Novo!')



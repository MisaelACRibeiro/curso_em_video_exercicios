print('Verificação de um número é primo')
total = 0
num = int(input('Digite um número: '))
for i in range(1, num + 1):
    if num % i == 0:
        print('\033[33m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print('{}'.format(i), end=' ')
print('\n\033[mO numero {} foi divisível {} vezes'.format(num, total))
if total == 2:
    print('Portanto é Primo')
else:
    print('Protanto não é Primo')
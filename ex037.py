print('Converção de Numeros')
num = int(input('Digite um numero inteiro: '))
print('''[1] Converte para Binário
[2] Converte para Octal
[3] Converte para Hexadecimal''')
resp = int(input('Digite a opção para converção: '))
if resp == 1:
    print('{} convertido para Binário é iqual a {}'.format(num, bin(num)[2:]))
elif resp == 2:
    print('{} convertido para Octal é iqual a {}'.format(num, oct(num)[2:]))
elif resp == 3:
    print('{} convertido para Hexadecimal é iqual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida')

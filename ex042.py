n1 = int(input('Digite o Primeiro seguimento: '))
n2 = int(input('Digite o Segundo segimento: '))
n3 = int(input('Digite o Terceiro seguimento: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Os seguimentos acima podem Formar um triangulo ', end='')
    if n1 == n2 == n3:
        print('EQUILÀTERO')
    elif n1 != n2 != n3 != n1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Não forma um triangulo')

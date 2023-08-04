'''Crie um program que leia dois valores e mostre um menu na tela
[1]Somar
[2]Multiplicar
[3]Maior
[4]Novos números
[5]Sair do Programa
Seu programa deverá realizar a operação solicitada em cada caso.'''

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o Segundo número: '))
escolha = 0
while escolha != 5:
    print('''    [1]Somar
    [2]Multiplicar
    [3]Maior
    [4]Novos números
    [5]Sair do Programa''')
    escolha = int(input('Qual é a sua escolha? '))
    if escolha == 1:
        print('A soma entre {} e {} é iqual á {}'.format(n1, n2, n1+n2))
    elif escolha == 2:
        print('A multiplicação entre {} e {} é iqual á {}'.format(n1, n2, n1*n2))
    elif escolha == 3:
        if n1 > n2:
            print('Entre {} e {} o número maior é {}'.format(n1, n2, n1))
        elif n1 < n2:
            print('Entre {} e {} o número maior é {}'.format(n1, n2, n2))
        else:
            print('Os números são iquais')
    elif escolha == 4:
        n1 = int(input('Digite novo primeiro número: '))
        n2 = int(input('Digite novo segundo número: '))
    elif escolha > 5:
        print('Digite uma opção válida: ')
print('Fim')

'''Crie um programa que leai vários númeroa inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi
o maior e menor valores lidos. o programa deve perguntar ao usuário se ele quer
ou não continuar a digitar valores.'''

n = 0
resposta = str('s')
cont = 0
soma = 0
maior = 0
menor = 0
while resposta not in 'N':
    n = int(input('Digite um número: '))
    resposta = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    cont += 1
    soma += n
    if n > maior:
        maior = n
    elif n < maior:
        menor = n
média = soma / cont
print('Você digitou {} números e a soma é {} e a média é {:.2f}'.format(cont, soma, média))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
print(f'O maior valor foi {maior} e o menor foi {menor}')

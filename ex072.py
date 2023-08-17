'''Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu program deverá ler um número pelo teclado (entre 0 a 20) e mostrá-lo por extenso.'''
numeros_extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco',
                   'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
                   'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze',
                   'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
num = int(input('Digite um Valor entre 0 e 20: '))
while num not in range(20):
    num = int(input('Atenção! Digite um Valor entre 0 e 20: '))
print(f'Você digitou o número {numeros_extenso[num]}')

#OUTRA FORMA DE FAZER

while True:
    valor = int(input('Digite um número entre 0 e 20: '))
    if 0 <= valor <= 20:
        break
    print('Atenção! ', end='')
print(f'Você digitou o número {numeros_extenso[valor]}')

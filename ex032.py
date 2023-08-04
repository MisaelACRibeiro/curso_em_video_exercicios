'''from datetime import date
ano = int(input('Digite um ano para verificar se ele é Bissexto ou Não: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} não é Bissexto'.format(ano))

n1 = int(input('digite o primeiro numero: '))
n2 = int(input('digite o segundo numero: '))
n3 = int(input('digite o terceiro numero: '))
lista = [n1, n2, n3]
id(lista)
lista.sort()
print('O maior numero é {}'.format(lista[2]))
print('O menor numero é {}'.format(lista[0]))

salario = float(input('Qual é o salário do funcionário? '))
if salario <= 1250:
    print('o aumento do salario R${:.2f} será de 10%, novo salario R${:.2f}'.format(salario, salario+(salario * 0.1)))
else:
    print('o aumento do salario R${:.2f} será de 15%, novo salario R${:.2f}'.format(salario, salario+(salario * 0.15)))
 ou
salario = float(input('Qual é o salário do funcionário? '))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('Quem ganhava R${:.2f} passsa a ganhar R${:.2f} '.format(salario, novo))'''


print('\033[1;97mOlá mundo!\033[m')
n1 = float(input('Primeiro seguimento: '))
n2 = float(input('Segundo seguimento: '))
n3 = float(input('Terceiro seguimento: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('\033[4;30;42mforma um triangulo\033[m')
else:
    print('Não forma um triangulo')

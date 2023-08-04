'''Crie um programa que simule o funcionamento de um caixa eletrônico. No final,
pergunte ao usuário qual será o valor a ser sacado(numero interio) e o programa
vai informar quantas cédulas de cada valor serão entregues
OSB: considere que o caixa possui cédulas de R$50, R$20, R$10, R$1.'''

num = int(input('Qual valor você quer sacar? R$ '))
nota50 = num // 50
if nota50 != 0:
    print(f'vão ser {nota50} notas de R$50')
sobra1 = num - (nota50 * 50)

nota20 = sobra1 // 20
if nota20 != 0:
    print(f'vão ser {nota20} notas de R$20')
sobra2 = sobra1 - (nota20 * 20)

nota10 = sobra2 // 10
if nota10 != 0:
    print(f'vão ser {nota10} nota de R$10')
sobra3 = sobra2 - (nota10 * 10)

nota1 = sobra3 // 1
if nota1 != 0:
 print(f'vão ser {nota1} notas de R$1')

#Usando WHILE TRUE

saque = int(input('Qual valor você quer sacar? R$'))
total = saque #total irá dimuir
cedula = 50
total_cedula = 0 #usado para contar as cedulas
while True:
    if total >= cedula:
        total -= cedula #Diminui o valor da cedula do valos total
        total_cedula += 1
    else:
        if total_cedula > 0:
            print(f'Vão ser {total_cedula} notas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        total_cedula = 0
        if total == 0:
            break
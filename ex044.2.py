print('{:=^40}'.format(' Loja 10 '))
valor = float(input('Qual é o valor da sua compra? R$ '))
print('''Selecione a forma de pagamento 
[1] Á vista Dinheiro/Cheque: 10% de desconto
[2] Á vista no cartão: 5% de desconto
[3] 2x no cartão: Preço normal
[4] 3x ou mais no cartão: 20% de juros''')
escolha = int(input('Digite sua opção: '))
if escolha == 1:
    total = valor - (valor * 10) / 100
    desc = 10
elif escolha == 2:
    total = valor - (valor * 5) / 100
    desc = 5
elif escolha == 3:
    total = valor
    desc = 0
elif escolha == 4:
    parc = int(input('\nQuantas vezes você quer quer parcelar? '))
    print('Vai ter 20% de JUROS')
    total = valor + (valor * 20) / 100
    desc = 0
print('\nSua compra de R${}\nVai ter um desconto de {}%\nVai ficar em R${}'.format(valor,desc, total))

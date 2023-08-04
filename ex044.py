print('{:=^40}'.format(' LOJA 10 '))
valor = float(input('Digite o valor da sua compra: R$ '))
print('''Selecione a forma de pagamento 
[1] Á vista Dinheiro/Cheque: 10% de desconto
[2] Á vista no cartão: 5% de desconto
[3] Em 2x no cartão: Preço normal
[4] Em 3x ou mais no cartão: 20% de juros''')
escolha = int(input('Digite sua opção: '))
if escolha == 1:
    print('O valor do produto será de R$ {:.2f}'.format(valor - (valor * 10) / 100))
elif escolha == 2:
    print('O valor do produto será de R$ {:.2f}'.format(valor - (valor * 5)/100))
elif escolha == 3:
    print('O valor do produto será de R$ {:.2f}'.format(valor))
elif escolha == 4:
    div = int(input('Informe em quantas parcelas você quer pagar: '))
    print('O valor da compra será de R$ {:.2f}'.format(valor + (valor * 20) / 100))
else:
    print('Escolha uma opção válida')

print('Verificação para compra de uma casa')
valor = float(input('Qual é o valor da casa? R$'))
salário = float(input('Qual é o seu salário? R$'))
anos = int(input('Digite em quantos anos você quer pagar? '))
prestação = valor / (anos * 12)
limite = (salário * 30) / 100
print('Para comprar uma casa de R${:.2f}, em {} anos a prestaçãp será de R${:.2f}'.format(valor, anos, limite))
if prestação <= limite:
    print('\033[1;30;42mAPROVADO\033[m')
else:
    print('\033[1;30;41mNEGADO\033[m')

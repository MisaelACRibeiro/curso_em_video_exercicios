print('Calculando o IMC')
peso = float(input('Informe o seu peso em Kg: '))
altura = float(input('Informe a sua altura: '))
imc = peso / altura ** 2
print('Seu IMC é de {:.1F}, '.format(imc), end="")
if imc < 18.5:
    print('Você está abaixo do Peso')
elif 18.5 <= imc < 25:
    print('Você está com peso Ideal!')
elif 25 <= imc < 30:
    print('Você está com Sobrepeso')
elif 30 <= imc < 40:
    print('Você está com Obesidade')
else:
    print('Você está com Obesidade mórbida')

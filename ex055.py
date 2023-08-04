maior = 0
menor = 0
for i in range(1, 4):
    peso = float(input('Digite o {}° valor: '.format(i)))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior é {} e o menor é {}'.format(maior, menor))

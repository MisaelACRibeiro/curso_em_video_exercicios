print('Detector de PALINDROMO')
frase = str(input('Digite um frase: '))
f1 = frase.lower().replace(' ', '')
fim = f1[::-1]
print('O inverso de {} é {}'.format(f1, fim))
if f1 == fim:
    print('É um palindromo')
else:
    print('Não é um palindromo')

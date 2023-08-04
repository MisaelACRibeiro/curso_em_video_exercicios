'''n = int(input('Digite um numero: '))
if  (n % 2) == 0:
    print(' o numero {} é par'.format(n))
else:
    print('o numero {} é Impar'.format(n))

d = float(input('Digite a Distancia da sua viagem em Km: '))
if d <= 200:
    print('Sua viagem de {} Km custará R$ {}'.format(d, d * 0.50))
else:
    print('Sua viagem de {} Km custará R$ {}'.format(d, d * 0.45))'''

d = float(input('Digite a distancia da sua viagem em KM:'))
if  d <= 200:
    preço = d * 0.50
else:
    preço = d * 0.45
print('Sua viagem de {}Km custará {}'.format(d, preço))

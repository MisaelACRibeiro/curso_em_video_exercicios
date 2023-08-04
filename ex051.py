print('{:=^40}'.format('Progressão Aritimética'))
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo = primeiro + (10 - 1) * razao
for i in range(primeiro, decimo + razao, razao):
    print('{}'.format(i), end=' → ')
print('ACADOU')

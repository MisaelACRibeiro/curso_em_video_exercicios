from datetime import date
ano = date.today().year
maior = 0
menor = 0
for pessoas in range(1, 4):
    nasc = int(input('Em que ano a {} pessoa nasceu: '.format(pessoas)))
    idade = ano - nasc
    if idade >= 18:
       maior += 1
    else:
        menor += 1
print('\nNo total são {} pessoas com Maior idade e {} Pessoas com Menor de idade'.format(maior, menor))

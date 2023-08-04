'''Melhore o Desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerra quando ele disser que quer mostrar 0 termos'''
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão termo: '))
termo = primeiro
contador = 1
mais = 10
total = 0
while mais != 0:
    total += mais
    while contador <= total:
        print('{}, '.format(termo), end='')
        termo += razao
        contador += 1
    print('PAUSA')
    mais = int(input('Quantos termo você quer mostrar a mais? '))
print('Progreção finalizada com {} termos'.format(total))
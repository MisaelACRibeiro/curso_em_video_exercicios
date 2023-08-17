'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
na ordem de colocação. Depois mostre:
A) Os 5 Primeiro.
B) Os últimos 4 colocados.
C) Times em Ordem alfabetica.
D) Em que posição está o time da Chapecoense.'''

times = ('Botafogo', 'Flamengo', 'Fluminense', 'Palmeiras', 'Bragantino', 'Grêmio', 'Athletico-PR', 'Cuiabá',
         'São Paulo', 'Atlético-MG', 'Cruseiro', 'Internacional', 'Fortaleza', 'Corinthians', 'Goiás', 'Bahia',
         'Santos', 'Coritiba', 'Vasco da Gama', 'América-MG')
verificacao = ('Chapecoense')
print(f'Os 5 Primeiros times são: {times[0:5]}',)
print(f'Os quatro últimos times são: {times[-4:]}')
print(f'Times em ordem alfabetica: {sorted(times)}')
if verificacao in times:
    print(f'O time {verificacao} está na {times.index(verificacao)+1}° posição')
else:
    print(f'O time {verificacao} não está entre os 20 primeiros ')

'''Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.'''
total = 0
produtos = ('Arroz', 20,
            'Feijão', 7,
            'Óleo de soja', 3,
            'Sal', 2.5,
            'Açúcar', 4,
            'Café', 12,
            'Molho de tomate', 2.75,
            'Macarrão', 5,
            'Milho', 3.5)
print('~'*30)
print(f'{"Lista de produtos":^30}')
print('~'*30)
for posiçao in range(0, len(produtos)):
    if posiçao % 2 == 0:
        print(f'{produtos[posiçao]:.<20}', end='')
    else:
        print(f'R${produtos[posiçao]:6.2f}')
        total += posiçao
print('~'*30)
print(f'{"Total":.<20}', end='',)
print(f'R${total:6.2f}')

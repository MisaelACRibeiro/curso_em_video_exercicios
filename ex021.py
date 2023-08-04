nome = str(input('Digite seu nome completo: '))
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
n = nome.split()
print('seu primeiro nome é {} e ele tem {} letras'.format(n[0], len(n[0])))


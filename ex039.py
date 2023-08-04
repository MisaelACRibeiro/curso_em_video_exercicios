from datetime import date
print('\033[4;97;42mVericação de Alistamento\033[m')
ano = int(input('Digite o ano do seu nascimento: '))
idade = date.today().year - ano
if idade < 18:
    print('Ainda falta {} anos para você se alistar'.format(18 - idade))
    print('Seu alistamento será em {}'.format(ano + 18))
elif idade == 18:
    print('Você tem {} anos está na hora de se alistar'.format(idade))
elif idade > 18:
    print('Já passou {} anos do alistamento'.format(idade - 18))
    print('Seu alistamento foi em {}'.format(ano + 18))

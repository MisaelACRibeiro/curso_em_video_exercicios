from datetime import date
data = int(input('Digita o ano do seu nascimento: '))
idade = date.today().year - data
print(idade)
if idade <= 9:
    print('Sua Categoria é MIRIN, você tem {}'.format(idade))
elif 9 < idade < 14:
    print('Sua categoria é INFANTIL, você em {}'.format(idade))
elif 14 < idade < 19:
    print('Sua categoria é JUNIOR, você tem {}'.format(idade))
elif 19 < idade < 20:
    print('Sua categoria é de SÊNIOR, você tem {}'.format(idade))
else:
    print('Sua cartegoria é de MASTER, você tem {}'.format(idade))

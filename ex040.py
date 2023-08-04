n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
média = (n1 + n2) / 2
print('Sua média foi de {:.1f}'.format(média))
if média < 5:
    print('Você foi \033[1;97;41mREPROVADO\033[m')
elif média >= 5 and média < 6.9:
    print('Você está de \033[1;30;43mRECUPERAÇÃO\033[m')
else:
    print('Você foi \033[1;97;44mAPROVADO\033[m')

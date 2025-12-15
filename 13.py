peso =int(input('digite o peso do peixe:'))
if peso > 50 :
    multas = (peso - 50) * 4
    print('total de multas :{}' .format(multas))
else:
    print('não teve excesso')
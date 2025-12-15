


print('digite suas notas de acordo com cada bimestre')

b1 = float(input('digite sua nota'))
b2 = float(input('digite sua nota'))
b3 = float(input('digite sua nota'))
b4 = float(input('digite sua nota'))

media = (b1 + b2 + b3 + b4 ) /4

if media < 7 :
    print('REPROVADO')
if media > 7 :
    print('APROVADO')

print('sua nota final é:',media)

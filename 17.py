nome = input('digite seu nome:' )
altura = float(input ('digite sua altura: '))
idade = int(input('digite sua idade: '))

if nome == 'messi' or (altura > 1.60 and idade > 17):
    print('joga no meu time')
else:
    print('infelizmente não vai ter como vc jogar no nosso time')
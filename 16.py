s1 = float(input('digite a distância do seu salto: '))
s2 = float(input('digite a distancia do seu salto: '))

if s1 > s2:
    print(f's1 ganhou com {s1} metros!')

elif s2 > s1:
    print(f's2 ganhou com {s2} metros!')

else:
    print('ambos empataram')
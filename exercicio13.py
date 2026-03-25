time01 = int(input('Quantos gols o primeiro time fez? '))
time02 = int(input('Quantos gols o segundo time fez? '))

if time01 > time02:
    print('O primeiro time venceu')

elif time01 < time02:
    print('O segundo time venceu')

else:
    print('Os dois times empataram')
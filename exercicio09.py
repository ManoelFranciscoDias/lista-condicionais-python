nota01 = float(input('Digite a primeira nota: '))
nota02 = float(input('Digite a segunda nota: '))

media = (nota01 + nota02) / 2

if media >= 6:
    print(f'Você foi aprovado com média {media}')

else:
    print(f'Você foi reprovado com média {media}')

    
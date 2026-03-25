nota01 = int(input('Digite a primeira nota: '))
nota02 = int(input('Digite a segunda nota: '))

media = (nota01 + nota02) / 2

if media >= 7:
    print(f'Aprovado')

else:
    exame = float(input('Digite a nota do exame: '))

    media_final = (media + exame) / 2

    if media_final >= 5:
        print(f'Aprovado')
    else:
        print(f'Reprovado')

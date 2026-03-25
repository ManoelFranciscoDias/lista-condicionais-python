nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 9 and media <= 10:
    print(f'notas: {nota1}; {nota2}')
    print(f'média: {media}')
    print('Conceito A')
    print('Aprovado')

elif media >= 7.5 and media < 9:
    print(f'notas: {nota1}; {nota2}')
    print(f'média: {media}')
    print('Conceito B')
    print('Aprovado')

elif media >= 6 and media < 7.5:
    print(f'notas: {nota1}; {nota2}')
    print(f'média: {media}')
    print('Conceito C')
    print('Aprovado')

elif media >= 4 and media < 6:
    print(f'notas: {nota1}; {nota2}')
    print(f'média: {media}')
    print('Conceito D')
    print('Reprovado')

elif media >= 0 and media < 4:
    print(f'notas: {nota1}; {nota2}')
    print(f'média: {media}')
    print('Conceito E')
    print('Reprovado')

else:
    print("Notas inválidas. Digite notas entre 0 e 10.")



#entrada
a = float(input('Digite o valor do lado A: '))
b = float(input('Digite o valor do lado B: '))
c = float(input('Digite o valor do lado C: '))

#processamento e saída
if (a < b + c) and (b < a + c) and (c < a + b):
    if (a == b == c):
        print('Triângulo Equilátero')

    elif (a == b) or (b == c) or (c == a):
        print('Triângulo Isóceles')

    elif (a != b != c):
        print('Triângulo Escaleno')

else:
    print('Erro!')



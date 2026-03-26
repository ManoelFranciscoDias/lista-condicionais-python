import math

# Entrada
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

# Processamento e saída
delta = b**2 - 4*a*c


if delta < 0:
    print("A equação não possui raízes reais.")

elif delta == 0:
    x = -b / (2 * a)
    print("A equação possui apenas uma raiz real.")
    print("Raiz:", x)

else:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print("A equação possui duas raízes reais.")
    print("Raiz 1:", x1)
    print("Raiz 2:", x2)

    
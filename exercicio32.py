n1 = int(input("Digite o primeiro valor inteiro: "))
n2 = int(input("Digite o segundo valor inteiro: "))

resto = n1 % n2

if resto == 1:
    resultado = n1 + n2 + resto
    print(f"Soma + resto: {resultado}")

elif resto == 2:
    if n1 % 2 == 0:
        print("Primeiro número é PAR")
    else:
        print("Primeiro número é ÍMPAR")

    if n2 % 2 == 0:
        print("Segundo número é PAR")
    else:
        print("Segundo número é ÍMPAR")

elif resto == 3:
    resultado = (n1 + n2) * n1
    print(f"(Soma * primeiro): {resultado}")

elif resto == 4:
    if n2 != 0:
        resultado = (n1 + n2) / n2
        print(f"(Soma / segundo): {resultado}")
    else:
        print("Erro: divisão por zero")

else:
    print(f"Quadrado do primeiro: {n1 ** 2}")
    print(f"Quadrado do segundo: {n2 ** 2}")
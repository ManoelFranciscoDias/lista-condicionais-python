numero = int(input("Digite um número de 4 dígitos: "))

if numero >= 1000 and numero <= 9999:
    parte1 = numero // 100
    parte2 = numero % 100 

    soma = parte1 + parte2

    if soma ** 2 == numero:
        print("O número atende à característica")
    else:
        print("O número NÃO atende à característica")
else:
    print("Número inválido (deve ter 4 dígitos)")


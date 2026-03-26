# entrada
valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
valor3 = float(input("Digite o terceiro valor: "))

# processamento e saída
if valor1 > valor2 and valor1 > valor3 and valor2 > valor3:
    print(f'A soma dos 2 maiores valores é: {valor1 + valor2}')

elif valor2 > valor1 and valor2 > valor3 and valor1 > valor3:
    print(f'A soma dos 2 maiores valores é: {valor2 + valor1}')

elif valor3 > valor1 and valor3 > valor2 and valor1 > valor2:
    print(f'A soma dos 2 maiores valores é: {valor3 + valor1}')

elif valor3 > valor1 and valor3 > valor2 and valor2 > valor1:
    print(f'A soma dos 2 maiores valores é: {valor3 + valor2}')

elif valor2 > valor1 and valor2 > valor3 and valor3 > valor1:
    print(f'A soma dos 2 maiores valores é: {valor2 + valor3}')

elif valor1 > valor2 and valor1 > valor3 and valor3 > valor2:
    print(f'A soma dos 2 maiores valores é: {valor1 + valor3}')

elif valor1 == valor2 and valor1 > valor3:
    print(f'A soma dos 2 maiores valores é: {valor1 + valor2}')

elif valor1 == valor3 and valor1 > valor2:
    print(f'A soma dos 2 maiores valores é: {valor1 + valor3}')

elif valor2 == valor3 and valor2 > valor1:
    print(f'A soma dos 2 maiores valores é: {valor2 + valor3}')

else:
    print("Os três valores são iguais.")



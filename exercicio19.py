# entrada
valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

# processamento e saída
if valor1 > valor2:
    print(f'{valor2}; {valor1}')

elif valor1 < valor2:
    print(f'{valor1}; {valor2}')

else:
    print("Os dois valores são iguais.")
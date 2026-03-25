valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
valor3 = float(input("Digite o terceiro valor: "))

if valor1 > valor2 and valor1 > valor3 and valor2 > valor3:
    print(f'{valor3}; {valor2}; {valor1}')

elif valor2 > valor1 and valor2 > valor3 and valor1 > valor3:
    print(f'{valor3}; {valor1}; {valor2}')

elif valor3 > valor1 and valor3 > valor2 and valor1 > valor2:
    print(f'{valor2}; {valor1}; {valor3}')

elif valor3 > valor1 and valor3 > valor2 and valor2 > valor1:
    print(f'{valor1}; {valor2}; {valor3}')

elif valor2 > valor1 and valor2 > valor3 and valor3 > valor1:
    print(f'{valor1}; {valor3}; {valor2}')

elif valor1 > valor2 and valor1 > valor3 and valor3 > valor2:
    print(f'{valor2}; {valor3}; {valor1}')

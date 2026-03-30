#entrada
salario = float(input('Informe o seu salario: '))

#processamento e saída
if salario < 10000:
    print(f'salario com reajuste: {salario * 1.55}')

else:
    print(f'salario com reajuste: {salario * 1.20}')



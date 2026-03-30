#entrada
salario = float(input('Digite o seu salário atual: '))

#processamento e saída
if (salario <= 400):
    print(f'Você recebeu um indice de aumento de 15%, seu salario agora é R${salario * 1.15}')

elif (400 < salario <= 700):
    print(f'Você recebeu um indice de aumento de 12%, seu salario agora é R${salario * 1.12}')

elif (700 < salario <= 1000):
    print(f'Você recebeu um indice de aumento de 10%, seu salario agora é R${salario * 1.10}')

elif (1000 < salario <= 1500):
    print(f'Você recebeu um indice de aumento de 7%, seu salario agora é R${salario * 1.07}')

elif (1500 < salario <= 2000):
    print(f'Você recebeu um indice de aumento de 4%, seu salario é agora é R${salario * 1.04}')

elif (salario > 2000):
    print(f'Você não recebeu aumento, seu salario permanece R${salario}')


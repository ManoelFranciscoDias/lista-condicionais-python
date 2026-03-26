# entrada
horas_prof01 = int(input('Digite as horas trabalhadas pelo primeiro professor: '))
horas_prof02 = int(input('Digite as horas trabalhadas pelo segundo professor: '))
valor_prof01 = float(input('Digite o valor da hora do primeiro professor: '))
valor_prof02 = float(input('Digite o valor da hora do segundo professor: '))

# processamento e saída
salario_prof01 = horas_prof01 * valor_prof01
salario_prof02 = horas_prof02 * valor_prof02

if salario_prof01 > salario_prof02:
    print('O primeiro professor tem um salário maior')

elif salario_prof01 < salario_prof02:
    print('O segundo professor tem um salário maior')

else:
    print('Os dois professores têm o mesmo salário')
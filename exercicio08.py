# entrada
idade = int(input('Digite a sua idade: '))

# processamento e saída
if idade < 18:
    print('Você é menor de idade')

elif idade >= 18 and idade < 65:
    print('Você é maior de idade')

else:
    print('Você tem mais de 65 anos')  
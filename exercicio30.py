temperatura = int(input('Qual a temperatura do aluminio em Celsius (°C): '))

if temperatura <= 1000:
    if temperatura <= 500:
        print(f'Temperatura Invalida')

    elif temperatura < 700 and temperatura > 500:
        print(f'Aquecimento ligado em 100%')

    elif temperatura < 735 and temperatura >= 700:
        print(f'Aquecimento ligado em 50%')

    elif temperatura >= 735 and temperatura <= 780:
        print(f'Aquecimento Desligado')

    else: 
        print(f'Superaquecimento')

else:
    print(f'Número Invalido, digite de 0 a 1000')
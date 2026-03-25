anoAtual = int(input('Qual o ano atual?? '))
anoNascimento = int(input('Digite o seu ano de nascimento: '))

idade = anoAtual - anoNascimento

if idade >= 16:
    print('Você pode votar')

else:
    print('Você não pode votar')



    
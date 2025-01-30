

#Desafio 56 - Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
tot = maior = woman = 0
velho = ''

for i in range(4):  
    #Cadastro das pessoas
    print(f'\n{" Pessoa" + str(i+1) + " ":=^30} ')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo[F/M]: ').strip().upper()

    #calcula a media de idade
    tot += idade
    media = tot / 4

    #mulheres com menos de vinte anos
    if sexo == 'F' and idade <= 20:
        woman += 1

    #Homem mais velho
    if sexo == 'M' and idade > maior:
         maior = idade
         velho = nome

print(f'\nMedia de idade é {media}\nHomem mais velho: {velho}\nMulheres com menos de 20 anos: {woman}')

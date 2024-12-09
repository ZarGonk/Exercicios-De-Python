#Desafio 51 - Desenvolva um programa que leia o primeiro termo e a razão de uma PA. 
# No final, mostre os 10 primeiros termos dessa progressão.
'''num = int(input('Informe o primerio termo: '))
pa = int(input('Qual a Razao: '))

print('\nOs 10 pimeiros termos são:\n')
for i in range(1 , 11):
  an = num + (i - 1) * pa
  print(an, end=' -> ')
print('ACABOU')
'''
#Desafio 52 - Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
'''num = int(input('Digite Um Numero Inteiro: '))

if num <= 1:
  print('Esse não e primo!')
elif num == 2 or num == 3:
  print('Ele é Primo !!!')
elif num % 2 == 0 or num % 3 == 0:
  print('O {} não e primo!'.format(num))
else:
  print('Esse numero é primo: {}'.format(num))
'''
#Desafio 53 - Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, 
# desconsiderando os espaços. 
# Exemplos: APOS A SOPA, A SACADA DA CASA, 
# A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.
'''frase = str(input('Qual Sua Frase: ')).upper()
frasejunta = frase.replace(' ','')

if frasejunta == frasejunta[::-1]:
  print('\nA frase é um Palindromo')
else:
  print('\nA frase não é um Palindromo')
print('\nO inverso da frase é: \n{}'.format(frasejunta[::-1]))
'''
#Desafio 54 - Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores. Considerando 21 anos.
'''from datetime import date

maior = 0
menor = 0

for i in range(0, 7):
  ano = int(input('Qual seu ano de nascimento: '))
  data = date.today().year
  idade = data - ano
  if idade >= 21:
    maior =+ 1
  else:
    menor =+ 1
print('São maior de idade: {}  \nSão menor de idade: {}'.format(maior, menor))
'''
#Desafio 55 - Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
'''maior = 0 
menor = 0

for i in range(0, 5):
  num = float(input('{} - Qual O seu peso (KG): '.format(i+1)))
  if i == 0:
    maior = num
    menor = num
  else:
    if maior <= num:
      maior = num
    elif menor >= num:
      menor = num
print('O maior peso é: {:.1f}Kg\nO menor peso é: {:.1f}Kg'.format(maior, menor))
'''
#Desafio 56 - Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
tot = 0
maior = 0
woman = 0
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

#Desafio 30 - Escreva um programa que leia a velocidade de um carro. Se ele ultrapassa 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
'''
vel = float(input("Velocidade do Carro: "))

if vel > 80:
  multa = (vel - 80) * 7
  print("Voce Foi Multado\n Valor: {:.2f}".format(multa))
else:
  print("Vai Traquilo!!!")
'''


#Desafio 33 - Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
'''
a = float(input('Digite primeiro numero: '))
b = float(input('Digite segundo numero: '))
c = float(input('Digite terceiro numero: '))

#Verifica o Menor
menor =  a
if (b < a) and (b < c):
  menor = b
if (c < a) and (c < b):
  menor = c

#Verifica o Maior
maior = a
if (b > a) and (b > c):
  maior = b
if (c > a) and (c > b):
  maior = c


print("O maior número é {}".format(maior))
print('O menor numero é {}'.format(menor))'''
#Desafio 34 - Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
'''
num = float(input('Digite o seu Salario: '))

if num >= 1250:
  aumento = num * 0.1
  saldo = num + aumento
  print('Seu Salario Vai Passar a Ser {}'.format())
else:
  aumento = num * 0.15
  saldo = num + aumento
  print('Seu Salario Vai Passar a Ser {}'.format())
'''
#Desafio 35 - Desenvolva um programa que leia o comprimento de tres retas e diga ao usuário se elas podem ou não formar um triângulo

a = float(input('Digite primeiro numero: '))
b = float(input('Digite segundo numero: '))
c = float(input('Digite terceiro numero: '))

if a < b + c and b < a + c and c < a + b:
  print('\nPode formar um tringulo')
else:
  print('\nNao forma um triangulo')

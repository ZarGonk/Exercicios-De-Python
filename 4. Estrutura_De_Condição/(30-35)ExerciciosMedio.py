#Desafio 30 - Escreva um programa que leia a velocidade de um carro. Se ele ultrapassa 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
'''
vel = float(input("Velocidade do Carro: "))

if vel > 80:
  multa = (vel - 80) * 7
  print("Voce Foi Multado\n Valor: {:.2f}".format(multa))
else:
  print("Vai Traquilo!!!")
'''



#Desafio 35 - Desenvolva um programa que leia o comprimento de tres retas e diga ao usuário se elas podem ou não formar um triângulo

a = float(input('Digite primeiro numero: '))
b = float(input('Digite segundo numero: '))
c = float(input('Digite terceiro numero: '))

if a < b + c and b < a + c and c < a + b:
  print('\nPode formar um tringulo')
else:
  print('\nNao forma um triangulo')

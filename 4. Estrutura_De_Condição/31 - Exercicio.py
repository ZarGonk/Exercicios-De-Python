# Desafio 31 - Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.
des = float(input('Distancia Da Viagem: '))

#Valor da Viagem se for menos que 200 KM
if des <= 200: 
  preço = des * 0.50
  print('O valor da sua viagem deu: R$ {:.2f}'.format(preço))
  
else: #Valor da viagem se for maior que 200KM
  preço = des * 0.45
  print('O valor da sua viagem deu: R$ {:.2f}'.format(preço))
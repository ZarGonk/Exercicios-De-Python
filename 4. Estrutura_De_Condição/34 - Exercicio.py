# Desafio 34 - Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

num = float(input('Digite o seu Salario: '))

if num >= 1250:
  aumento = num * 0.1
  saldo = num + aumento
  print('Seu Salario Vai Passar a Ser {}'.format())
else:
  aumento = num * 0.15
  saldo = num + aumento
  print('Seu Salario Vai Passar a Ser {}'.format())
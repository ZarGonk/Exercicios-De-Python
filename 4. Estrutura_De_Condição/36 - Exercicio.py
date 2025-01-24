#Desafio 36 - Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela nao pode exceder 30% do salário ou então o empréstimo será negado.

valor_casa = float(input("Qual o Valor da Casa? "))
salario = float(input("Qual o Seu Salario? "))
q_anos = int(input("Em Quantos Anos Pretende Quitar a Casa? "))

#Calcula As Parcelas Que Devem Ser Pagas 
total = (( valor_casa / q_anos ) / 12 )
#Calcula Os 30% do Salario
negado = salario * 0.30

if total >= negado:
  print('Seu Salar io Não Atinge Aos Nossos Criterios\nO valor das parcelas ficaria {}'.format(total))  
else:
  print('As prestações vão ser {:.2f} por mes,Durante {}'.format(total, q_anos))

#Desafio 41 - A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade: - Até 9 anos: MIRIM - Até 14 anos: INFANTIL - Até 19 anos: JÚNIOR - Até 25 anos: SÊNIOR - Acima: MASTER.
'''from datetime import date
data = int(input('Qual seu ano de Nascimento: '))
ano = date.today().year
idade = ano - data

if idade <= 9:
  print('Voce tem {} anos então pertence a categoria Mirim'.format(idade))
elif idade <= 14:
  print('Voce tem {} anos então pertence a categoria Infantil'.format(idade))
elif idade <= 19:
  print('Voce tem {} anos então pertence a categoria Junior'.format(idade))
elif idade <= 25:
  print('Voce tem {} anos então pertence a categoria Senior'.format(idade))
else:
  print('Voce tem {} anos então pertence a categoria Master'.format(idade))
'''
#Desafio 42 - Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado: - Equilátero: todos os lados iguais - Isósceles: dois lados iguais - Escaleno: todos os lados diferente.
'''
a = float(input('Digite primeiro numero: '))
b = float(input('Digite segundo numero: '))
c = float(input('Digite terceiro numero: '))

#verifica se pode formar um trinagulo
if a < b + c and b < a + c and c < a + b:
  print('\nPode formar um tringulo')
  #Verifica o tipo do triangulo
  if a == b == c:
    print('\nEsse triangulo é Equilatero')
  elif a == b or b == c or a == c:
    print('\nEsse trinagulo é Isosceles')
  else:
    print('\nEsse triangulo é Escaleno')
else:
  print('\nNao forma um triangulo')
'''
#Desafio 43 - Desenvolva uma lógica que leia o peso e a altura de uma pessoa,calcule seu IMC e mostre seu status, de acordo com a tabela abaixo: - Abaixo de 18.5: Abaixo do peso - Entre 18.5 e 25: Peso ideal - 25 até 30: Sobrepeso - 30 até 40: Obesidade - Acima de 40: Obesidade mórbida.
'''peso = float(input('Qual seu peso: '))
altura = float(input('Qual sua altura: '))

imc = peso / (altura * altura)

if imc < 18.5:
  print('Seu IMC é {:.2f}, esta abaixo do peso'.format(imc))
elif 18.5 <= imc < 25:
  print('Seu IMC é {:.2f}, PARABENS!!! voce esta no peso ideial')
elif 25 <= imc < 30:
  print('Seu IMC é {:.2f}, esta com sobrepeso'.format(imc))
elif 30 <= imc < 40:
  print('Seu IMC é {:.2f}, TA OBESO FERA !!!'.format(imc))
else:
  print('Seu IMC é {:.2f}, SE VAI MORRER EM ta uma BALEIA'.format(imc))
'''
#Desafio 44 - Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento: - à vista dinheiro/cheque: 10% de desconto - à vista no cartão: 5% de desconto - em até 2x no cartão: preço normal - 3x ou mais no cartão: 20% de juros.

preco = float(input('Qual o preco normal do produto: '))

print('\nQual a forma de pagamento: ')
paga = int(input('\n[ 1 ] - A Vista Dinhero \n[ 2 ] - A vista no cartão \n[ 3 ] - 2x no cartão\n[ 4 ] - 3x ou mains no cartão\n\nQual Sua Opção ? '))


if paga == 1:
  ajuste = preco * 0.1
  dinheiro = preco - ajuste
  print('\nA vista no dinheiro fica \033[1;32mR$ {:.2f}\033[m, por conta do desconto de 10%'.format(dinheiro))
elif paga == 2:
  ajuste = preco * 0.05
  dinheiro = preco - ajuste
  print('\nA vista no cartão fica \033[1;32mR$ {:.2f}\033[m, por conta do desconto de 5%'.format(dinheiro))
elif paga == 3:
  parcela = preco / 2
  print('\nO valor das Parcelas vai ficar: R$ {:.2f} A vista no cartão fica \033[1;32mR$ {:.2f}\033[m'.format(parcela, preco))
  
elif paga == 4:
  ajuste = preco * 0.2
  dinheiro = preco + ajuste
  num = int(input('Quantas Parcelas Ira Fazer: '))
  parcela = preco / num
  print('\n{}X no cartão fica \033[1;32mR$ {:.2f}\033[m, por conta dos juros 20%\nE o Preco de cada parcela sera R$ {:.2f}'.format(num, dinheiro, parcela))

  
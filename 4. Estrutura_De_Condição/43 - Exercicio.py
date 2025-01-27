# Desafio 43 - Desenvolva uma lógica que leia o peso e a altura de uma pessoa,calcule seu IMC e mostre seu status, de acordo com a tabela abaixo: - Abaixo de 18.5: Abaixo do peso - Entre 18.5 e 25: Peso ideal - 25 até 30: Sobrepeso - 30 até 40: Obesidade - Acima de 40: Obesidade mórbida.

peso = float(input('Qual seu peso: '))
altura = float(input('Qual sua altura: '))

imc = peso / (altura * altura)

if imc < 18.5:
  print('Seu IMC é {:.2f}, IH qual foi magrão'.format(imc))
elif 18.5 <= imc < 25:
  print('Seu IMC é {:.2f}, PARABENS!!! voce esta no peso ideial')
elif 25 <= imc < 30:
  print('Seu IMC é {:.2f}, esta com sobrepeso'.format(imc))
elif 30 <= imc < 40:
  print('Seu IMC é {:.2f}, TA OBESO FERA !!!'.format(imc))
else:
  print('Seu IMC é {:.2f}, SE VAI MORRER EM ta uma BALEIA'.format(imc))

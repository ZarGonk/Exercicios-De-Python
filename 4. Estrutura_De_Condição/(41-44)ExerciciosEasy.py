


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

  
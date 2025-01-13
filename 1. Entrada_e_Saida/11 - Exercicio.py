#Desafio 11 - Crie um programa que leia quanto dinheiro uma pessoa tem, quantos dolares ela consegue comprar com esse dinheiro
#considerando R$ 1.00 = R$ 3.27
dinheiro = float(input("Quanto a na sua carteira ?"))
dolar = dinheiro / 3.27

print("Você consegue compra: {:.2f}".format(dolar))

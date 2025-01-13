#Desafio 9 - crie um programa que converta metros em centímetros e milimetros
m = int(input("Digite um valor em metros: "))

cm = m * 100
mm = m * 1000

print("agora ele esta em: \nCentimetros: {}\nMilimetros: {}".format(cm, mm))

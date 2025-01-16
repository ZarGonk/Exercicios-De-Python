#Desafio 14 - Crie um programa que leio o salario de um funcionario, e mostre seu novo salario com 15% de aumento

v = float(input("qual é o seu salario? "))

aumento = v * 0.15
salario = v + aumento

print("Seu salario agora é: {:.2f}".format(salario))

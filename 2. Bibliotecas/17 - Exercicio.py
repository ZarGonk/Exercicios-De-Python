#Desafio 17 - faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa
#DICA: math.hypot

from math import hypot

v1 = float(input("Diga seu A: "))
v2 = float(input("Diga seu B: "))
hip = hypot(v1, v2)

print("o Valor da sua Hipotenisa é: {:.2f}".format(hip))
#Desafio 18 - faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo
import math

ang = float(input("Informe o angulo: "))
ang_rad = math.radians(ang)

coss = math.cos(ang_rad)
sen = math.sin(ang_rad)
tang = math.tan(ang_rad)

print("Do seu angulo {} aqui esta:\nCosseno: {:.2f}\nSeno: {:.2f}\nTangente: {:.2f}".format(ang, coss, sen, tang))
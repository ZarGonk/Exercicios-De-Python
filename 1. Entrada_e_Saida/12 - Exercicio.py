#Desafio 12 - Crie um programa que leia a altura e a lagura de uma parede em metros, calcule a area total, e a quantidade necessaria de tinta para pintar esta parede, sabendo que cada litro de tinta pinta 2m^2
alt = float(input("qual a altura da parede: "))
lar = float(input("qual a largura da parede: "))

area = alt * lar

quant_tinta = area / 2

print("Area total da parede {} m² e quantidade de tinta para pintar {}".format(area, quant_tinta))

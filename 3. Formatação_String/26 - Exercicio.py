# Desafio 26 - faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a ultima vez.

f = str(input("digite sua frase: ")).strip()
min = f.lower()


print("Quantos (A) tem: {}\nPrimeira posicao: {}\nUltima posicao: {}".format(min.count("a"), min.find("a"), min.rfind("a")) )

# Exercício 75: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#   Quantas vezes apareceu o valor 9.
#   Em que posição foi digitado o primeiro valor 3.
#   Quais foram os números pares.

num1 = int(input('Digite 1 valor: '))
num2 = int(input('Digite 1 valor: '))
num3 = int(input('Digite 1 valor: '))
num4 = int(input('Digite 1 valor: '))

tupla = (num1, num2, num3, num4)

#Quantas vezes o 9 apareceu e se apareceu
if 9 in tupla:
    nove = tupla.count(9)
    print(f'O 9 apareceu {nove} vezes')
else:
    print('Não teve ocorrência só 9')

#Qual posição o 3 apareceu e se apareceu    
if 3 in tupla:
    tres = tupla.index(3)+1
    print(f'primeira aparição do 3: {tres}°')
else:
    print('Numero 3 não foi encontrado')    

#Ve se tem par e mostra se tiver
print(f'Numero Par: ') 
for i in tupla:
    if i % 2 == 0:
        print(i ,end=' ')  


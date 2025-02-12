# Exercício 85: Crie um programa onde o usuário possa digitar sete valores 
#numéricos e cadastre-os em uma lista única que mantenha separados os 
#valores pares e ímpares. No final, mostre os valores pares e ímpares em 
#ordem crescente.
number = [[], []]
for i in range(7):
    num = int(input('Enter a number: '))

    if num % 2 == 0:
        number[0].append(num)
    else:
        number[1].append(num)
number[0].sort()
number[1].sort()

print(f'The even values entered were: {number[0]}')
print(f'The odd entered were: {number[1]}')

def par(num=0):
    if num % 2 == 0:
        return True
    return False

#Codigo principal

n = int(input('Digite um numero: '))

if par(n):
    print('Este numero é Par')
else:
    print('Este numero é impar') 
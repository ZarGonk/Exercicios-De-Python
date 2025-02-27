# Exercício 113: Reescreva a função leiaInt() que fizemos no Exercício 104, incluindo agora a possibilidade da digitação de um número de tipo inválido.Aproveite e crie também a função leiaFloat() com a mesma funcionalidade.
#   Exemplo:

#   n = leiaInt('Digite um número inteiro: ')
#   f = leiaFloat('Digite um número real: ')
#   print(f'Você acabou de digitar o número inteiro {n} e o número real {f}')
import numeros

# Código principal
n = numeros.leiaInt('Digite um número Inteiro: ')
f = numeros.leiaFloat('Digite um número Real: ')

print('~' * 30)
print(f'Número Inteiro: {n}\nNúmero Real: {f:.2f}')
print('~' * 30)

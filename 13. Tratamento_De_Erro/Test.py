try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a/b

except (ValueError, TypeError):
    print('Tivemos problemas com os dados informados')
except ZeroDivisionError:
    print('Não é possivel fazer divisão com denominador ZERO')
except KeyboardInterrupt:
    print('O Usuario prefiriu não informar os dados')
    
else:
    print(f'O resultado é {r:.1f}')

finally:
    print('Volte sempre! Muito obrigado')

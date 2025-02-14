#Exercício 92: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário. 
# Se, por acaso, a CTPS for diferente de 0, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime
dados = dict()

#dados caso nao tenha carteira de trabalho
dados['Nome'] = str(input('Nome: '))

ano = int(input('Ano de nascimento: '))
ano_atual = datetime.now().year
dados['Idade'] = ano_atual - ano

#dados caso haja carteira de trabalho
dados['Carteira'] = int(input('Carteira de trabalho(0 - nao tem): '))
if dados['Carteira'] != 0:
    dados['Ano De Contrataçao'] = int(input('Ano de contrataçao: '))
    dados['Salario'] = float(input('Salario: '))

    #aposentadoria
    dados['Aposentadoria'] = (dados['Ano De Contrataçao'] - ano) + 35
#Gera os dados cadastrados
print(f'\n=-=-=-=-Dados De {dados["Nome"]}-=-=-=-=')
for c, v in dados.items():
    print(f'{c}: {v}')
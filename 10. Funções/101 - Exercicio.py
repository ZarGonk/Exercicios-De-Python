# Exercício 101: Crie um programa que tenha uma função chamada voto(), que vai receber como parâmetro o ano de nascimento de uma pessoa e retornar um valor indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.
def voto(nascimento=0):
    from datetime import date
    date_att = date.today().year
    idade = date_att - nascimento

    if idade < 16:
        return f'Idade: {idade}\nVoto: NEGADO'

    elif 16 <= idade < 18 or idade > 65:
        return f'Idade: {idade}\nVoto: OPCIONAL'

    else:
        return f'Idade: {idade}\nVoto: OBRIGATORIO'


#Codigo principal
nascimento = int(input('Informe data do seu nascimento: '))
print(voto(nascimento))
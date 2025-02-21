# Exercício 105: Faça um programa que tenha uma função chamada notas(), que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:

#Quantidade de notas.
#A maior nota.
#A menor nota.
#A média da turma.
#A situação (opcional), que pode ser: "boa", "razoável" ou "ruim".

def notas(*nota, sit=False):
    """
    ->Função analisa notas e situacão de um aluno
    :param *nota: uma ou mais notas de um aluno (aceita varias)
    :param sit: Valor opcional, Indica a situação que se encontra o aluno
    :return: Dicionario com as informações registradas do aluno
    """
    boletim = dict()
    boletim["Total"] = len(nota)
    boletim["Maior"] = max(nota)
    boletim["Menor"] = min(nota)
    boletim["Media"] = sum(nota)/ len(nota)

    if sit == True:
        if boletim['Media'] > 7:
            boletim["Situação"] = 'BOA'
        elif 6 <= boletim['Media'] < 7:
            boletim['Situação'] = 'RAZOAVEL'
        else:
            boletim['Situação'] = 'RUIM'
    return boletim

resp = notas(2.5, 1.5, 2)
print(resp)

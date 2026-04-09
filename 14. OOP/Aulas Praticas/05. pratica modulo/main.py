from rich import inspect
from classes import Aluno, Professor, Funcionario


a1 = Aluno('José', 17, 'Informatica', "T01")

p1 = Professor('Samual', 37, 'Biologia', 'Mestre')

f1 = Funcionario('Sonia', 25, 'Secretaria', 'Secretaria')

## Aluno
a1.fazer_aniversario()
a1.fazer_matricula()
inspect(a1)

## Professor
p1.dar_aula()
inspect(p1)

## Funcionário
f1.fazer_aniversario()
f1.bater_ponto()
inspect(f1)

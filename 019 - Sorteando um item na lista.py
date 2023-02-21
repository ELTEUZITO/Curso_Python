from random import choice

aluno1 = str(input("1° Aluno: "))
aluno2 = str(input("2 Aluno: "))
aluno3 = str(input("3° Aluno: "))
aluno4 = str(input("4° Aluno: "))

lista = [aluno1, aluno2, aluno3, aluno4]
escolhido = choice(lista)

print("O escolhido foi {}".format(escolhido))

from random import shuffle

aluno1 = str(input("1° Aluno: "))
aluno2 = str(input("2° Aluno: "))
aluno3 = str(input("3° Aluno: "))
aluno4 = str(input("4° Aluno: "))

lista = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista)

print("A lista sera ")
print(lista)
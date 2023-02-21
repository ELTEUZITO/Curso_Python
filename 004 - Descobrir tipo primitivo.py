co = input("Digite algo: ")

print("------ Vamos descobrir o tipo primitivo ------")

print("Sua classe é... ")
print(type(co))

print("{} é um numero? {}".format(co, co.isnumeric()))
print("{} é uma letra? {}".format(co, co.isalpha()))
print("{} está maiúsculo? {}".format(co, co.isupper()))
print("{} está minúsculo? {}".format(co, co.islower()))

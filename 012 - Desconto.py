prod = float(input("Preço: R$"))

dess = prod - (prod * 5 / 100)

print("Seu preço original era de R${} ".format(prod))
print("e agora com o seu desconto seu novo preço e de R${:.2f}.".format(dess))

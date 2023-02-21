fun = float(input("Seu sálario: R$"))

novo = fun + (fun * 15 / 100)

print("Seu sálario antigo era de R${} e agora com 15% de aumento você vai receber R${:.2f}.".format(fun, novo))

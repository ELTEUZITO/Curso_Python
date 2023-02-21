lag = float(input("Qual a largura? "))
alt = float(input("Qual a altura? "))

area = lag * alt
tin = area / 2

print("Com {}m de largura e a altura de {}m você vai precisar de {:.2f}L de tinta.".format(lag, alt, tin))

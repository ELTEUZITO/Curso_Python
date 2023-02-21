dias = int(input("Dias alugado: "))
rodado = float(input("KM rodados: "))

pagar = (dias * 60) + (rodado * 0.15)

if pagar > 1300 :
    desc = pagar - (pagar * 3 / 100)
    print("O total a pagar deu R${:.2f}, vamos te dar um desconto de 3% agora o valor é R${:.2f}!".format(pagar, desc))

print("Total a pagar será de R${:.2f}.".format(pagar))

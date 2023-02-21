from math import sin, cos, tan, radians

ang = float(input("Digite o ângulo: "))

se = sin(radians(ang))
co = cos(radians(ang))
ta = tan(radians(ang))

print("Seu SENO seria {:.2f} \nSeu COSSENO seria {:.2f} \nSua TANGENTE seria {:.2f}".format(se, co, ta))

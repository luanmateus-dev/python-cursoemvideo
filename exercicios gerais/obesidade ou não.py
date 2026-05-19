atual= float(input("qual o seu peso em KG? "))
altura= float(input("qual sua altura em Metros? "))
peso= atual/altura**2
print("vc pesa atualmente {:.1f} KG!".format(peso))
if peso<18.5:
    print("ABAIXO DO PESO!!")
elif peso<25:
    print("PESO IDEAL!!")
elif peso<30:
    print("SOBREPESO!!")
elif peso<40:
    print("OBESIDADE!!")
else:
    print("OBESIDADE MÓRBIDA")


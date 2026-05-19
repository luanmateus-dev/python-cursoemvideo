from datetime import date
atual= date.today().year
nasc= int(input("qual ano vc nasceu? "))
idade= atual-nasc
print("quem nasceu em {}, tem {} anos, no ano de {}".format(nasc,idade,atual))
if idade==18:
    print("vc precisa se alistar imediatamente!")
elif idade>18:
    saldo= idade-18
    print(" vc ja deveria ter alistado a {} anos atrás ".format(saldo))
else:
    saldo= 18-idade
    print("falta ainda  {} anos para vc poder se alistar".format(saldo))



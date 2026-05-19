km= float(input("qual a distancia da sua viagem? "))
if km <=200:
    valor= km * 0.50
else:
    valor= km * 0.45
print(" sua viagem foi de {}KM e vc pagara RS{:.2f} reais!".format(km,valor))



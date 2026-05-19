from datetime import date
totmaior= 0
totmenor= 0
atual= date.today().year
for c in range(1,8):
    nu= int(input("em que ano a {}° nasceu? ".format(c)))
    idade= atual-nu
    if idade>=21:
        totmaior +=1
    else:
        totmenor +=1
print("temos {} pessoas de maior".format(totmaior))
print("e temos {} pessoas de menor".format(totmenor))




from datetime import date
ano= date.today().year
nasci= int(input("ano de nascimento: "))
idade= ano-nasci
print("o atleta tem {} anos. ".format(idade))
if idade <=9:
    print("classificação: Mirim")
elif idade >=10 and idade <=14:
    print("classificação: Infantil")
elif idade >=15 and idade <=19:
    print("classificação: Junior")
elif idade >=20 and idade <=25:
    print("classificação: Sênior")
else:
    print("classificação: Master")



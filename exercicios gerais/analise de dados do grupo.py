maior=conthomem=totmulher20=0
while True:
    idade= int(input("idade: "))
    sexo=' '
    while sexo not in 'MF':
        sexo= str(input("sexo: ")).strip().upper()[0]
    continuar=' '
    while continuar not in 'SN':
        continuar= str(input("quer continuar? [S/N] ")).strip().upper()[0]
    if idade>=18:
        maior+=1
    if sexo=="M":
        conthomem+=1
    if sexo=="F" and idade<20:
        totmulher20+=1
    if continuar=="N":
        break
print(f"total de pessoas com mais de 18: {maior}")
print(f"ao todo temos {conthomem} homens cadastrados")
print(f"e temos {totmulher20} mulheres menores de 20 anos")







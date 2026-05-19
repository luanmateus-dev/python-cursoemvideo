somaidade=0
mediaidade=0
maioridadehomem=0
maisvelho=''
totmulher20=0
for c in range(1,5):
    print("---------{}°PESSOA---------".format(c))
    nome= str(input("nome: ")).strip()
    idade= int(input("idade: "))
    sexo= str(input("sexo [M/F]: ")).strip()
    somaidade +=idade
    if sexo in "fF" and idade<20:
        totmulher20 += 1
    if c==1 and sexo in "Mm":
        maioridade=idade
        maisvelho=nome
    if sexo in "Mm" and idade>maioridadehomem:
        maioridadehomem=idade
        maisvelho=nome
mediaidade= somaidade/4
print(" a média das idades e igual a {} ".format(mediaidade))
print(" o mais velho tem {} anos e se chama {}".format(maioridadehomem,maisvelho))
print("ao todo são {} mulheres menores de 20 anos".format(totmulher20))

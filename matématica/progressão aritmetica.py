nu1= int(input('digite o primeiro termo: '))
nu2= int(input('digite a razão: '))
termo= nu1
cont=1
while cont<=10:
    print("{}  ".format(termo),end='')
    termo+=nu2
    cont+=1

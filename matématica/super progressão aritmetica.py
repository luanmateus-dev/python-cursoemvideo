nu1= int(input("primeiro termo: "))
nu2= int(input("razão: "))
termo=nu1
cont=1
total=0
mais=10
while mais!=0:
    total+=mais
    while cont<=total:
        print("{} -> ".format(termo),end='')
        termo+=nu2
        cont+=1
    print("PAUSA ")
    mais= int(input("quantos termos você quer mostrar a mais? "))
print("finalizado... com {} termos mostrados ".format(total))
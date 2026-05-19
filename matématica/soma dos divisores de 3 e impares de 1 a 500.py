s=0
cont= 0
for c in range(1,501,2):
    if c%3==0:
        print(c)
        s+=c
        cont+=1
print("a soma dos {} numeros que são divisores de 3 e impares de 1 a 500 é igual a= {} ".format(cont, s))
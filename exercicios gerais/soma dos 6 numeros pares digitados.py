s=0
cont=0
for c in range(1,7):
    nu= int(input("digite o {}º numero: ".format(c)))
    if nu % 2 ==0:
        s+=nu
        cont+=1
print(" a soma dos {} numeros pares que foi digitado é igual a = {} ".format(cont,s))






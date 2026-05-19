cont=0
s=0
n=0
while n!=999:
    n = int(input("digite um numero [999 para parar]: "))
    if n!=999:
        s+=n
        cont+=1
print(f"você digitou {cont} numeros e a soma entre eles foi de {s}")

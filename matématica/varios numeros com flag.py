n=cont=s=0
while True:
    n= int(input("digite um numero: "))
    if n == 999:
        break
    cont+=1
    s+=n
print(f"você digitou {cont} numeros e a soma deles é {s}. ")
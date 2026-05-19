resp= 'S'
cont= soma= media= maior = menor =0
while resp in 'Ss':
    n= int(input("digite um numero: "))
    cont+=1
    soma+=n
    if cont==1:
        maior=menor=n
    else:
        if n>maior:
            maior=n
        if n<menor:
            menor=n
    resp= str(input("quer continuar? [S/N]")).strip().upper()[0]
media= soma/cont
print("você digitou {} numeros e a media foi {:.2f}".format(cont,media))
print("o maior numero é o {} e o menor numero é o {}".format(maior,menor))
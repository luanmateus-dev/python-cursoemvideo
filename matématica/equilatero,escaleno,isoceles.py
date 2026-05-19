a= float(input("primeiro segmento: "))
b= float(input("seugundo segmento: "))
c= float(input("terceito segmento: "))
if a+b>c and a+c>b and b+c>a:
    print("os segmentos acima podem formar um triangulo!!",end=" ", )
    if a==b==c:
        print("Equilatero!")
    elif a!=b!=c!=a:
        print("Escaleno!")
    else:
        print("Isoceles")
else:
    print("os segmentos acima não formam um triangulo!!")



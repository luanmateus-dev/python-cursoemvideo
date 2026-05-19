print("_"*30)
print("sequência de fibonacci")
print("_"*30)
n= int(input("quantos termos deseja mostrar? "))
print("_"*30)
t1=0
t2=1
cont=3
print("{}=>".format(t1,t2),end='')
while cont<=n:
    t3=t1+t2
    t1=t2
    t2=t3
    cont+=1
    print("{} => ".format(t3),end='')
print("FIM")
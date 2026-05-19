nu= int(input("digite um numero para calcular sua fatorial: "))
c= nu
f=1
print("calculando {}! = ".format(nu),end='')
while c>0:
    print("{}".format(c),end='')
    print(' x ' if c>1 else ' = ' ,end='')
    f*=c
    c-=1
print('{}'.format(f))

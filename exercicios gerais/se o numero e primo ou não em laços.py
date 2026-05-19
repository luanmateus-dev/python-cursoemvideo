nu= int(input("digite um numero: "))
tot= 0
for c in range(1,nu+1):
    if nu%c==0:
        print("\033[34m",end=" ")
        tot+=1
    else:
        print("\033[31m",end=" ")
    print("{} ".format(c), end=" ")
print("\n\033[mo numero {} foi divisivel {} vezes".format(nu,tot))
if tot==2:
    print("é por isso ele é PRIMO!")
else:
    print("é por isso que ele NÃO É PRIMO!")




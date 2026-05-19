nu1= int(input("digite um numero inteiro: "))
print("""escolha sua conversão: 
[1] converter para binario
[2] converter para octal
[3] converter para hexadecimal""")
opção= int(input("a sua escolha é: "))
if opção==1:
    print("{} sua conversão para binario e igual a {}".format(nu1,bin(nu1)[2:]))
elif opção==2:
    print("{} sua conversão para octal é igual a {} ".format(nu1, oct(nu1)[2:]))
elif opção==3:
    print("{} sua conversão para hexadecimal é igual a {} ".format(nu1, hex(nu1)[2:]))
else:
    print("opção invalida. Tente novamente.")





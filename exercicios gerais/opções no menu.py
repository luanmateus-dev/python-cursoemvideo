from time import sleep
nu1= int(input("digite o primeiro valor:  "))
nu2= int(input("digite o segundo valor; "))
opcao=0
while opcao !=5:
    print("""    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos numeros
    [5] sair do programa""")
    opcao= int(input("qual a sua opção? "))
    if opcao==1:
        soma=nu1+nu2
        print("==================================")
        print("a soma dos dois valores é igual a {}".format(soma))
        print("==================================")
    elif opcao==2:
        multiplicar=nu1*nu2
        print("==================================")
        print("a multiplicação dos dois valores é igual a {}".format(multiplicar))
        print("==================================")
    elif opcao==3:
        if nu1>nu2:
            print("==================================")
            print("dos dois valores o numero {} é o maior".format(nu1))
            print("==================================")
        elif nu1==nu2:
            print("==================================")
            print("os dois valores são iguais")
            print("==================================")
        else:
            print("==================================")
            print("dos dois valores o numero {} é o maior".format(nu2))
            print("==================================")
    elif opcao==4:
        print("==================================")
        print("informe os numeros novamente!!")
        print("==================================")
        nu1= int(input("digite o primeiro valor: "))
        nu2= int(input("digite o segundo valor: "))
    sleep(2)
print("==================================")
print("fim do programa...")
print("==================================")

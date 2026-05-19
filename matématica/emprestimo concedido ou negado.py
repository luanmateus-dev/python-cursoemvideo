nu1= float(input("qual o valor da casa? "))
nu2= float(input("quanto vc ganha por mês? "))
nu3= int(input("quantos anos de financiamento? "))
mini= nu2*30/100
prestação= nu1/ (nu3 * 12)
print(" para vc pegar uma casa de {:.2f} e {} anos de prestação sera de {:.2f}".format(nu1,nu3,prestação))
if prestação<=mini:
    print("seu emprestimo foi concedido!")
else:
    print("seu emprestimo foi negado!")




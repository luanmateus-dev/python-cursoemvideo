print("=======LOJA LUAN=======")
gastou= float(input("qual o valor da compra: R$ "))
print("""FORMA DE PAGAMENTO
 [1] a vista dinheiro/cheque
 [2] a vista cartão 
 [3] 2x no cartão
 [4] 3x ou mais no cartão""")
opção= int(input("qual é a opção? "))
if opção==1:
    total= gastou- (gastou*10/100)
elif opção==2:
    total= gastou- (gastou*5/100)
elif opção==3:
    total= gastou
    parcela = total/2
    print("\033[1;34msua compra com parcela de 2x foi de R${:.2f}\033[m ".format(parcela))
elif opção==4:
    total=gastou + (gastou*20/100)
    totparcelas= int(input("Em quantas parcelas? "))
    parcela= total/totparcelas
    print(" \033[1;34msua compra de {}x foi de R${:.2f}\033[m ".format(totparcelas,parcela))
else:
    total=0
    print("\033[1;31mopção invalida de pagamento. tente novamente!")
print("\033[1;31msua compra de R${:.2f} vai custar R${:.2f} no final.".format(gastou, total))



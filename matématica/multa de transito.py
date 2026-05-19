v= float(input("qual foi a velocidade em que passou no radar? "))
if v>80:
    print(" vc foi multado, passou do limite de 80KM/H")
    multa= (v-80) * 7
    print(" vc tera que pagar RS{:.2f} reais de multa ".format(multa))
    print(" pare de correr igual louco!!")
print(" bom dia, dirija com segurança!")

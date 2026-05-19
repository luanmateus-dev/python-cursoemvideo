frase= str(input("digite a frase: ")).strip().lower() #tira os espaços inuteis. #coloca tudo em minusculo
palavra= frase.split() #separa em blocos
junto= "".join(palavra) #junta as palavras que vc separou em blocos
inverso= ""
for letra in range(len(junto)-1,-1,-1):
    inverso+= junto[letra]
print("o inverso de {} é {}".format(junto,inverso))
if inverso==junto:
    print("ESSA FRASE É UM PALINDROMO!")
else:
    print("ESSA FRASE NÃO É UM PALIMDROMO!")
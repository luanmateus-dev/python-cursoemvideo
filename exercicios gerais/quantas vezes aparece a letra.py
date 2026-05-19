frase= str(input("digite uma frase: ")).lower().strip()
print(" A letra A aparece {} vezes na frase:".format(frase.count("a")))
print(" A letra A aparece na primeira posição {}: ".format(frase.find("a")+1))
print(" A letra A aparece na ultima posição {}: ".format(frase.rfind("a")+1))


from random import randint
computador = randint(0, 5)
jogador = int(input(" qual numero eu pensei? entre 0 ao 5: "))
if computador == jogador:
    print("PARABENS!! VC ACERTOU O NUMERO QUE EU PENSEI!!")
else:
    print(" VC PERDEU!! EU PENSEI NO NUMERO {} ".format(computador))

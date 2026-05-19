from random import randint
computador = randint(0,10)
print("pensei em um numero de 0 a 10: ")
print("será que vc consegue adivinhar? ")
acertou = False
palpite=0
while not acertou:
    jogador= int(input("qual seu palpite? "))
    palpite+=1
    if computador==jogador:
        acertou = True
    else:
        if jogador<computador:
            print("MAIS....TENTE MAIS UMA VEZ.")
        else:
            print("MENOS...TENTE MAIS UMA VEZ.")
print("ACERTOU com {} alternativas. PARABENS!!".format(palpite))

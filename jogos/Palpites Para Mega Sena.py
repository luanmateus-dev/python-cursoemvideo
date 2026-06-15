from random import randint
from time import sleep
lista = list()
jogos = list()
print("=" *30)
print("      JOGA MEGA SENA       ")
print("=" *30)
tot = 1
quant = int(input("quantos jogos você quer sortear? "))
while tot <= quant:
    cont = 0
    while True:
        num = randint(0,60)
        if num not in lista:
            lista.append(num)
            cont+=1
            if cont >= 6:
                break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot +=1
for i , l in enumerate(jogos):
    print(f"jogo {i+1}: {l} ")
    sleep(1)



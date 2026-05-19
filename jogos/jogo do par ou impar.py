from random import randint
v=0
while True:
    computador= randint(0,10)
    jogador= int(input("digite um valor: "))
    escolha=' '
    while escolha not in 'PI':
        escolha= str(input("par ou impar? [P/I] ")).upper().strip()[0]
    s= jogador+computador
    print(f"você digitou {jogador} e o computador {computador} e o total foi {s} ",end='')
    print("DEU PAR" if s%2==0 else "DEU IMPAR")
    if escolha=="P":
        if s%2==0:
            print("VOCÊ VENCEU!!")
            v+=1
        else:
            print("VOCÊ PERDEU!!")
            break
    elif escolha =="I":
        if s%2==1:
            print("VOCÊ VENCEU!!")
            v+=1
        else:
            print("VOCÊ PERDEU!!")
            break
print(f"GAME OVER!! VOCÊ VENCEU {v} VEZES. TENTE NOVAMENTE, QUEM SABE GANHE NA PROXIMA!!")


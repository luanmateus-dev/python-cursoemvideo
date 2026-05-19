from random import randint
from time import sleep
itens= ("pedra", "papel", "tesoura")
computador= randint(0,2)
print("""[0] pedra
[1] papel
[2] tesoura""")
jogador= int(input("qual sua escolha: "))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!")
print("="*30)
print(" o computador escolheu {} ".format(itens[computador]))
print(" o jogador escolheu {} ".format(itens[jogador]))
print("="*30)
if computador==0:
    if jogador==0:
        print("EMPATE!")
    elif jogador==1:
        print("JOGADOR VENCEU!")
    elif jogador==2:
        print("COMPUTADOR VENCEU!")
    else:
        print("JOGADA INVÁLIDA")
elif computador==1:
    if jogador==0:
        print("COMPUTADOR VENCEU!")
    elif jogador==1:
        print("EMPATE!")
    elif jogador==2:
        print("JOGADOR VENCEU!")
    else:
        print("JOGADA INVÁLIDA!")
else:
    if jogador==0:
        print("JOGADOR VENCEU!")
    elif jogador==1:
        print("COMPUTADOR VENCEU!")
    elif jogador==2:
        print("EMPATE!")
    else:
        print("JOGADA INVÁLIDA")
print("="*15)
print("JOGO ENCERRADO!")




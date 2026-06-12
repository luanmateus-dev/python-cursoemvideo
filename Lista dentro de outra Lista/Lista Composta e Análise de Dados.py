dados = list()
galera = list()
cont = maior = menor = 0
while True:
    dados.append(str(input("nome: ")))
    dados.append(float(input("peso: ")))
    continuar = str(input("quer continuar? [S/N]: ")).strip().upper()[0]
    if len(galera) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    galera.append(dados[:])
    dados.clear()
    cont+=1
    if continuar == "N":
        break
print(f"Você cadastrou {cont} pessoas.")
print(f"O maior peso foi de {maior}KG peso de ",end='')
for p in galera:
    if p[1] == maior:
        print(f"[{p[0]}] ",end='')
print()
print(f"O menor peso foi de {menor}KG peso de ",end='')
for p in galera:
    if p[1] == menor:
        print(f"[{p[0]}] ",end='')


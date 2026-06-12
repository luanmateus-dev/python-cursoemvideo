dados = [[] , [] ]
valor = 0
for i in range(1,8):
    valor = int(input(f"digite o {i}° valor: "))
    if valor % 2 == 0:
        dados[0].append(valor)
    else:
        dados[1].append(valor)
dados[0].sort()
dados[1].sort()
print(f"Os valores pares digitados foram {dados[0]} ")
print(f"Os valores impares digitados foram {dados[1]} ")



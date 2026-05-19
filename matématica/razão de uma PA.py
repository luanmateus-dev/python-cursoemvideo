primeiro= int(input("digite o primeiro termo: "))
razao= int(input("digite a razão: "))
decimo= primeiro + (10-1) * razao
for c in range(primeiro,decimo+razao,razao):
    print("{} ".format(c),end=" ")


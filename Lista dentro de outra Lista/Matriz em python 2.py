Matriz = [[0,0,0] , [0,0,0] , [0,0,0] , [0,0,0]]
somapar = somaterceira = maiorsegunda = 0
for l in range (0,3):
    for c in range(0,3):
        Matriz[l][c] = int(input(f"Digite um valor para [{l},{c}]: "))
for l in range(0,3):
    for c in range(0,3):
        print(f" [{Matriz[l][c]:^5}] ",end='' )
        if Matriz[l][c] % 2 == 0:
            somapar+=Matriz[l][c]
    print()
for l in range(0,3):
    somaterceira+=Matriz[l][2]
for c in range(0,3):
    if c == 0:
        maiorsegunda = Matriz[1][c]
    elif Matriz[1][c] > maiorsegunda:
        maiorsegunda = Matriz[1][c]
print(f"A soma dos pares digitados foram {somapar} ")
print(f"A soma dos valores da terceira coluna é {somaterceira} ")
print(f"O maior valor da segunda linha é {maiorsegunda} ")








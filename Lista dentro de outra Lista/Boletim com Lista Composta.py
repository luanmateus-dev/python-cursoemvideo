ficha = list()
while True:
    nome = str(input("nome: "))
    nota1 = float(input("nota 1: "))
    nota2 = float(input("nota 2: "))
    media = (nota1+nota2)/2
    ficha.append([nome , [nota1, nota2] , media] )
    resp = str(input("quer continuar? [S/N]: ")).upper()
    if resp == "N":
        break
print(f"{"N°":<5} {"Nome":<5} {"MÉDIA":>10}")
print("-"*30)
for i, a in enumerate(ficha):
    print(f"{i:<5} {a[0]:<5} {a[2]:>10} ")
while True:
    print("-"*30)
    opc = int(input("Mostrar notas de qual aluno? [999 interrompe]: "))
    if opc == 999:
        break
    if opc <= len(ficha) - 1:
        print(f"notas {ficha[opc][0]} são {ficha[opc][1]} ")







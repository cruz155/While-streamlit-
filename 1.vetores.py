import os
os.system("cls")

#inserindo nota
for i in range(3):
    nota = int(input(f"Digite a {i+1}ª nota: "))
    soma += nota

    #mostrar notas 
    print(f"Nota: {nota}")
    print(f"Soma: {soma}")

    print("FIM")


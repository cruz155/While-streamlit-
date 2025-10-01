#criando um vetor(lista)
listas_notas=[]
#inserir notas
for i in range (3):
    nota=int(input(f"digite [i+1] nota:"))
    listas_notas.append(nota)
    
media=sum(listas_notas)/3
    #mostrar notas
print("\nresultados:")
for i in range(3):
        print(f"nota: {listas_notas}:")
    

print(f"media:{media}")

print("fim")
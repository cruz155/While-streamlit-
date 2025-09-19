import os
os.system("cls")


quantidade_pares = 0
quantidade_impares = 0
soma_pares = 0
soma_geral = 0
contador_total = 0


while True:
    numero = int(input("Digite um número inteiro positivo (ou 0 para encerrar): "))

    if numero == 0:
        break  
    elif numero < 0:
        print("Por favor, digite um número positivo ou zero.")
        

   
    if numero % 2 == 0:
        quantidade_pares += 1
        soma_pares += numero
    else:
        quantidade_impares += 1

  
    soma_geral += numero
    contador_total += 1


media_pares = soma_pares / quantidade_pares if quantidade_pares > 0 else 0
media_geral = soma_geral / contador_total if contador_total > 0 else 0


print(f"\nResultados:")
print(f"Quantidade de números pares: {quantidade_pares}")
print(f"Quantidade de números ímpares: {quantidade_impares}")
print(f"Média dos valores pares: {media_pares:.2f}")
print(f"Média geral dos números lidos: {media_geral:.2f}")
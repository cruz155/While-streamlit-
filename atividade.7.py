

pares = 0
impares = 0
soma_pares = 0
soma_total = 0
qtd_total = 0

while True:
    num = int(input("Digite um número inteiro positivo (0 para sair): "))
    if num == 0:
        break
    if num < 0:
        print("Digite apenas números positivos.")
        continue
    qtd_total += 1
    soma_total += num
    if num % 2 == 0:
        pares += 1
        soma_pares += num
    else:
        impares += 1

if pares > 0:
    pares = soma_pares / pares
else:
    media_pares = 0

if qtd_total > 0:
    media_geral = soma_total / qtd_total
else:
    media_geral = 0

print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")
print(f"Média dos valores pares: {media_pares:.2f}")
print(f"Média geral dos números lidos: {media_geral:.2f}")
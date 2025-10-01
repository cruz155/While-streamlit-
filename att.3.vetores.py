import os
os.system("cls")

# Programa que lê 5 números, armazena em um vetor, informa o menor, o maior
# e mostra todos os números informados pelo usuário

# Lê 5 números do usuário e armazena em uma lista
numeros = []
for i in range(5):
    numero = float(input(f'Digite o {i+1}º número: '))
    numeros.append(numero)

# Encontra o menor e o maior número
menor = min(numeros)
maior = max(numeros)

# Mostra os resultados
print("Números informados:", numeros)
print("Menor número:", menor)
print("Maior número:", maior)
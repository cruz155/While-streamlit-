import os
os.system("cls")

import os

# Lista para armazenar os dados das pessoas
pessoas = []

while True:
    print("Código | Descrição")
    print("1      | Adicionar pessoa")
    print("2      | Exibir resultados")
    print("3      | Sair")

    opcao = int(input("Escolha uma opção: "))

    match opcao:
        case 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            idade = int(input("Digite a idade: "))
            sexo = input("Digite o sexo (M/F): ").strip().upper()
            while sexo not in ['M', 'F']:
                sexo = input("Sexo inválido. Digite M ou F: ").strip().upper()
            salario = float(input("Digite o salário: "))
            pessoas.append({'idade': idade, 'sexo': sexo, 'salario': salario})
            input("Pressione Enter para continuar...")
            os.system('cls' if os.name == 'nt' else 'clear')

        case 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            if len(pessoas) == 0:
                print("Nenhuma pessoa cadastrada.")
            else:
                soma_salario = 0
                idades = []
                mulheres_5k = 0
                for p in pessoas:
                    soma_salario += p['salario']
                    idades.append(p['idade'])
                    if p['sexo'] == 'F' and p['salario'] >= 5000:
                        mulheres_5k += 1
                media_salario = soma_salario / len(pessoas)
                maior_idade = max(idades)
                menor_idade = min(idades)
                print(f"Média de salário do grupo: R$ {media_salario:.2f}")
                print(f"Maior idade do grupo: {maior_idade}")
                print(f"Menor idade do grupo: {menor_idade}")
                print(f"Quantidade de mulheres com salário a partir de R$ 5.000,00: {mulheres_5k}")
            input("Pressione Enter para continuar...")
            os.system('cls' if os.name == 'nt' else 'clear')

        case 3:
            print("Encerrando o programa.")
            break

        case _:
            print("Opção inválida. Tente novamente.")
            os.system('cls' if os.name == 'nt' else 'clear')
          

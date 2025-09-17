import os
os.system("cls")

login_cadastrado = "xereca123"
senha_cadastrado = "pulse123"

while True:
    login = input("Digite seu login: ")
    senha= input("Digite sua senha: ")
    

    if login == login_cadastrado and senha == senha_cadastrado:

        print("login correto")
        break
    else:
        tentativa += 1 
        print(F"tentativa{tentativa} de 3.")
        
        if tentativa == 3:
            print("Voce atingiu o maximo de tentativas")

import os
os.system("cls")

login_cadastrado = "usuario123"
senha_cadastrado = "senha123"

while True:
    login = input("Digite seu login: ")
    senha= input("Digite sua senha: ")
    

    if login == login_cadastrado and senha == senha_cadastrado:

        print("Bem vindo!")
        break
    else:
        print("Login ou senha inválidos")

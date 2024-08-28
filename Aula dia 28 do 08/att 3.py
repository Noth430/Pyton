import os 
os.system("cls || clear")

while True:
    login:str
    senha:str
    login = input("digite o longi")
    senha = input("Digite a senha ")

    if (senha == "123") and (login == "henrique"):
        print("Bem-vindo")
        break
    else:
        os.system("cls || clear")  
        print("tente novamente")


import os 
os.system("cls || clear")

contador = 0

while True:
    login:str
    senha:str
    contador += 1
    login = input("digite o longi")
    senha = input("Digite a senha ")

    if (senha == "123") and (login == "henrique"):
        print("Bem-vindo")
        break
    else:
        print(f"Tentativa: {contador}")
        if contador == 3:
            break
        
os.system("cls || clear")  
print("tente novamente")

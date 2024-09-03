import os 
os.system("cls || clear")

senha = input("digite uma senha")
while True:
    confirmacao = input("Digite a senha novamente: ")

    if senha == confirmacao:
        print("Senha correta: ")
        break
    else:
        print("Senha Incorreta")
                        
                        
    


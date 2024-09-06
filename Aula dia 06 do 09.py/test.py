import os 
os.system("cls || clear")


def definição_numero(n1):
    if n1 % 2 == 0:
        print("Numero par")   
    else:
        print("Numero impar ")

        

numero = int(input("Digite um numero: "))


resposta = definição_numero(numero)

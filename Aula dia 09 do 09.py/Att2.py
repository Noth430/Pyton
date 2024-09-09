import os 
os.system("cls || clear")

ano_nascimento = int(input("Digite seu ano de nascimento: "))

def idade(n1):
    ano_atual = 2024
    subtração = ano_atual -  n1

    return subtração

idade1 = idade(ano_nascimento)

print(f"Idade: {idade1}")

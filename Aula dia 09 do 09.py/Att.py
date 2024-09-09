import os
os.system("cls || clear")


def media(n1,n2):
    soma = n1 + n2
    media = soma/2

    return media

def valor_numero(n1,n2):

    if n1 >= 7:
        print("Aluno Aprovado: ")
    else:
        print("Reprovado: ")
    
    return n1,n2

numero1 = float(input("Digite uma nota: "))

numero2 = float(input("Digite uma nota: "))

resultado = media(numero1,numero2)

resultado2 = valor_numero(numero1,numero2)

print(f"Média: {resultado}")

print(f"Nota: {resultado2}")
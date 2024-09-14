import os
os.system("cls || clear")

lista_vetores = []


def operacao(numeros):
    if not numeros:
        return 0
    
    soma = sum(numeros) # sum usado para substituir soma
    media = soma/len (numeros) # len usado para sobstituir media

    return media


for i in range(4):
    numero = int(input(f"Digite o {i+1} numero: "))
    lista_vetores.append(numero)

media1  = operacao(lista_vetores)

for numero in lista_vetores:
    print(numero)

print(f"Media: {media1}")

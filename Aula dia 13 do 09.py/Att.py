import os
os.system("cls || clear")

lista_vetores = []
def verificacao(num):
    negativo = []
    for numero in num:
        
        if numero <0:
            numero = 0
            negativo.append(numero)       
        
    return negativo

for i in range(5):
    nota = float(input(f"Digite o {i+1} nota: "))
    lista_vetores.append(nota)

lista_vetores = verificacao(lista_vetores)

for nota in lista_vetores:
    print(nota)




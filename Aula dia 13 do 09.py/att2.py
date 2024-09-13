import os
os.system("cls || clear")

lista_vetores = []

def verificacao(numeros):
   
    
    for numero in numeros:

        maior_numero = max(lista_vetores)
        
    
        menor_numero = min(lista_vetores)
    return maior_numero,menor_numero

for i in range(6):
    nota = float(input(f"Digite o {i+1} nota: "))
    lista_vetores.append(nota)

lista_vetores = verificacao(lista_vetores)

for nota,maior_numero,menor_numero in lista_vetores:
    print(nota)
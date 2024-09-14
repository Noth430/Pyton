import os
os.system("cls || clear")

lista_vetores = []

def verificacao1(numeros):
    par = []
    impar = []
    
    for numero in numeros:
        if numero % 2 == 0:
            par.append(numero)
        else:
            impar.append(numero) 
    return par,impar       

def verificacao(numeros):
   
    if not numeros:
        return None, None           
        
    maior = max(lista_vetores)
        
    
    menor = min(lista_vetores)
    return maior,menor

for i in range(6):
    nota = float(input(f"Digite o {i+1} nota: "))
    lista_vetores.append(nota)

maior,menor = verificacao(lista_vetores)

pares,impares = verificacao1(lista_vetores)

print(f"Maior número: {maior}")
print(f"Menor número: {menor}")
print(f"Números pare: {pares}")
print(f"Numero impares: {impares}")
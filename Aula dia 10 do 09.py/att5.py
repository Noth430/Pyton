import os 
os.system("cls || clear")

notas = []
pares = 0
impares = 0

def verificacao(numeros):
    
    for numero in numeros:
        if nota % 2 == 0:
            pares +=1
        else:
            impares +=1
    return pares,impares

for i in range(6):
    nota = float(input("Digite uma nota: "))
    notas.append(nota)

pares, impares = verificacao(notas)

print(f"Quantidade pares: {pares}")
print(f"Quantiade impares: {impares}")


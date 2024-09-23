import os 
os.system("cls || clear")

print(""""
Crie um algoritmo que leia 5 números inteiros e,em seguida,mostre na tela:

1.Aquantidade de números pares e ímpares;
2.A quantidade de números positivos é negativos;
3.A quantidade de números inseridos.

""")

QUANTIDADE_NUMEROS = 5
pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(5):
    numero = int(input(f"Digite o {i+1}: "))

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    if numero <0:
        negativos += 1
    else:
        positivos +=1

print(f"Números pares {pares}: ")    
print(f"Números impares {impares}: ")
print(f"Positivos {positivos}: ")
print(f"Negativos {negativos}: ")
print(f"Quantidade de numeros insetidos {QUANTIDADE_NUMEROS}:")


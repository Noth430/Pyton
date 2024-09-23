"""
Crie um algoritmo que leia 5 números inteiros e, em seguida, usando funções, calcule e mostre na tela:

1. A quantidade de números pares e ímpares;
2. A quantidade de números positivos e negativos;
3. O maior e o menor número;
4. A média de números pares;
5. A média de números ímpares;
6. A média de todos o números inseridos;
7. A quantidade de números inseridos;
8. Mostrar os números lidos na ordem inversa;



"""
import os 
import random
os.system("cls||clear")

QTD= 5
lista=[]

for i in range (QTD):
    num=random.randint(-5,1)
    lista.append(num)

def impar_par(a):
    list_par=[]
    list_impar=[]
    for numero in a:
        if numero %2 == 0:
            list_par.append(numero)
        else:
            list_impar.append(numero)
    return list_par, list_impar
def positivo_negativo(a):
    lista_positivo = []
    lista_negativo = []
    for numero in a:
        if numero >0:
            lista_positivo.append(numero)
        else:
            lista_negativo.append(numero)
    return lista_positivo,lista_negativo


        
def media_impar(a):
    QNTD = len(a)
    soma = sum(a)
    for numero in a:
        if (numero >= 0) or (numero<=0):
                media = soma/QNTD
                return media 
        else:
            return 0

def media_par(a):
    QNTD = len(a)
    soma = sum(a)
    for numero in a:
        if (numero >= 0) or (numero<=0):
            media = soma/QNTD
            return media 
        else:
            return 0
lista_atualizada_positivo, lista_atualizada_negativo = positivo_negativo(lista)
lista_atualizada_par, lista_atualizada_impar = impar_par(lista)

soma_numero_inseridos = sum(lista)
soma_par = sum(lista_atualizada_par)
soma_impar = sum(lista_atualizada_impar)

media_impar0 = media_impar(lista_atualizada_impar)
media_par0 = media_par(lista_atualizada_par)



media = soma_numero_inseridos / QTD

max_num = max(lista)        
min_num = min(lista)

print(f"\033[4;35m=== Exibindo quantidade de números pares e impares ===\033[m")
print(f"\033[33mQuantidade de pares: {len(lista_atualizada_par)}")
print(f"Quantidade de impares: {len(lista_atualizada_impar)}")
print(f"\n=== Exibindo quantidade de positivos, negativos e inseridos ===")
print(f"Quantidade de positivos: {len(lista_atualizada_positivo)}")
print(f"Quantidade de negativos: {len(lista_atualizada_negativo)}")
print(f"Quantidade de números inseridos: {QTD}")
print("\n=== Exibindo maior e menor número ===")
print(f"Maior número: {max_num}")
print(f"Menor número: {min_num}")
print("\n=== Médias ===")
print(f"Média par: {media_par0}")
print(f"Média impar: {media_impar0}")
print(f"Média dos números inseridos: {media}")
total = len(lista)
for i, numero in enumerate(reversed(lista)):
    print(f"Reverso dos números: {total-i}º {numero}")
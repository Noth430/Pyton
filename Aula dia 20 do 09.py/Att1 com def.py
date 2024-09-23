import os

os.system("cls || clear")

QUANTIDADE_NUMEROS = 5
lista_numeros = []

def impares (lista_numeros):
    impares = 0
    for cada_numero in lista_numeros:
        if cada_numero % 1 ==0:
            impares +=1
    return impares
def pares(lis_numero):
    pares = 0
    for cada_numero in lis_numero:
        if cada_numero % 2 ==0:
            pares +=1
    return pares
def positivo(lis_numero):
    positivos = 0
    for cada_numero in lis_numero:
        if cada_numero >0:
            positivos +=1
    return positivos
def negativo(lista_numero):
    negativos = 0
    for cada_numero in lista_numero:
        if cada_numero <0:
            negativos +=1
    return negativos

for i in range(QUANTIDADE_NUMEROS):
        numero = int(input(f"Digite o {i+1}º numero: "))
        lista_numeros.append(numero)

quantiada_pares,quantiadade_impares = pares,impares(numero)

quantidade_positivos,quantidade_negativos = positivo,negativo(numero)

print(f"Quantidade de números pares: {quantiada_pares}")
print(f"Quantidade de números impares: {quantiadade_impares}")
print(f"Quantidade de números positivos: {quantidade_positivos}")
print(f"Quantidade de números negativo: {quantidade_negativos}")
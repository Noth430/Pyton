import os 
os.system("cls || clear")
Lista_numeros = []
positivo = []
negativo = []
QUANTIDADE_NOTAS = 4

for i in range(QUANTIDADE_NOTAS):
    
    numero = float(input("Digite um numero: "))
    Lista_numeros.append(numero)

    if numero < 0:
        positivo.append(numero) # Inserindo numero negativo 
    else:
        positivo.append(numero)

quantidade_negativos = len(negativo)

soma_positivo = sum(negativo)

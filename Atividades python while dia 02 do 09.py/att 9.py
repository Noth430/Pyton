import os 
os.system("cls || clear")

impares = 0
contador = 0

while impares <= 200:
    numero = int(input("digie um numero inteiro"))

    if numero % 2 != 0:
        impares += numero
        contador += 1

    print(f"numero digitado: {impares}")    


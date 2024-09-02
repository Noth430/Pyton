import os 
os.system("cls || clear")

numero_negativo = 0

while True:

    numero = float(input("Digite um numero"))

    if numero >0:
        break
    numero_negativo += 1

    print(f"quantidade de numeros negativos: {numero_negativo}")
    
        

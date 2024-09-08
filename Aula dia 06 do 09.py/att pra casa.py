import os
import time
os.system("cls||clear")
 
valor_original = float(input("Digite um valor: "))

def flacionação(valor_novo):

    if valor_original < 100:    
        valor_novo = valor_original * 1.10
    else:
        valor_novo = valor_original * 1.20
    
    return valor_novo


valor_original = flacionação(valor_original)

print(f"Preço: {valor_original}")
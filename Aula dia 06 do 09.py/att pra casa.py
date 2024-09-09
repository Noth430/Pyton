import os

os.system("cls||clear")
 
valor_original = float(input("Digite um valor: "))

def flacionação(valor_novo):

    if valor_original < 100:    
        valor_novo = (valor_original * 0.1) + valor_novo
    else:
        valor_novo = (valor_original * 1.2) + valor_novo
    
    return valor_novo


valor_original = flacionação(valor_original)

print(f"Preço: {valor_original:.2f}")

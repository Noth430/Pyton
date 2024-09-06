import os 
os.system("cls || clear")

def tabuada(n1):
    for i in range(1,11):
        print(f"{n1} x {i} = {n1 * i} ")

    return tabuada

numero = int(input("Digite um numero para tabuada"))  

valor_tabuada = tabuada(numero)


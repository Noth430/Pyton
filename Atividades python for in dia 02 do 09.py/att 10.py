import os 
os.system("cls || clea")

impares = 0
soma = 0
for numero in range (1,10,2):
    print(f"{numero}")
    if numero % 2 != 0:
        soma += numero

print(f"Impares: {impares}")
print(f"Soma: {soma}")
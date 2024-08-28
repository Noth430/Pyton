import os 
os.system("cls || clear")
pares = 0
impares = 0
for i in range(5):
    numero = int(input(f"digite um numero"))

    if numero % 2 == 0: # caso queira impa numero % 2 == 1:
        pares = pares + 1
    else:
        impares = impares + 1

print(f"{pares} pares  é  {impares}impares")

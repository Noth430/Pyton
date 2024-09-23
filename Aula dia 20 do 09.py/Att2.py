import os
os.system("cls || clear")


pares = 0
impares = 0
positivos = 0
negativos = 0

while True:
        numero = int(input("Digite um numero")) 
        
        if numero % 2 == 0 and numero >0:
            pares += 1

        elif numero % 2 != 0:
            impares += 1
        if numero <0:
            negativos += 1
        else:
            positivos +=1
        if numero == 0:
             break


print(f"Números pares positivos {pares}: ")    
print(f"Números impares {impares}: ")
print(f"Positivos {positivos}: ")
print(f"Negativos {negativos}: ")

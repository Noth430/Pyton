import os 
import time
os.system("cls || clear")
soma = 0
for i in range(3):
    notas = float(input("digitre uma nota"))
    soma = soma + notas
media = soma / 3

if notas >= 7 :
    print("aprovado")
else:
    if notas < 7 and notas >= 4 :
        print("recuperação")
    else:
        print("reprovado")

 
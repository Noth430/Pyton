import os

os.system("cls||clear")

soma=0

for i in range(1):
    while True:
        
     nota=float(input(f"Informe a {i+1}º nota: "))
     soma = soma+nota
     print(f"Sua media é {soma/3}")

          
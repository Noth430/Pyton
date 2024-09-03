import os 
os.system("cls || clear")

soma = 0
media = 0

while True:
    nota1 = float(input("Digite uma nota"))
    nota2 = float(input("Digite uma nota"))
    
    if nota1 >0 and nota2 >0: 
        print(f"Nota 1: {nota1} Nota 2: {nota2} ")

        soma += nota1 + nota2
        media = soma/2
    
    
    else: 
            nota1 <0 and nota2 <0
            print("Nota invalida")
        

    print(f"Media: {media}")   






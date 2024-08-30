import os 
os.system("cls || clear")

while True:
    nota = float(input("dgite uma nota"))
    
    if nota < 0 or nota > 10:
        print("\nA nota deve ser maior ou igual a 0 e menor e igual a 10")
    else:
        break # Para o laço de repetição

print(f"Nota: {nota}")        
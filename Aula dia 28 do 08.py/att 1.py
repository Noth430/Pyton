import os 
os.system("cls || clear")


nota = int(input("digite uma nota"))

while  nota <=0 or nota >=10:
    print("\nA nota deve ser maior  ou igual a 10 e maior ou igual a 0 ")
    nota = float(input("digite uma nota:"))

print(f"Nota: {nota}")  
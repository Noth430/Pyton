import os 
os.system("cls || clear")
soma = 0

for i in range(4):
    notas = float(input("digitre uma nota"))
    soma = soma + notas
media = soma / 4
print(f"a media é  {media} ")

import os
os.system("cls || clear")

notas = []

for i in range(3):
    nota = float(input("Digite uma nota: "))
    notas.append(nota)

for nota in notas:
    print(nota)
import os
os.system("cls || clear")
soma = 0
notas = []
contagem = 3
for i in range(3):
    nota = float(input("Digite uma nota: "))
    notas.append(nota)

soma = sum(notas)
media = soma/contagem


print(notas)

print(f"Media: {nota}")
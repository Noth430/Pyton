import os
os.system("cls || clear")
soma = 0
notas = []
contagem = 4
for i in range(4):
    nota = float(input("Digite uma nota: "))
    notas.append(nota)

soma = sum(notas)
media = soma/contagem

if media >=7:
    print("Aprovado: ")
elif media >=5:
    print("Recuperação: ")
else:
    print("Reprovado: ")

print(notas)

print(f"Media: {nota}")
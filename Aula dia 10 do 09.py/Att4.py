import os
os.system("cls || clear")

notas = []

for i in range(5):
    nota = float(input(f"Digite o {i+1} nota: "))
    notas.append(nota)

maior_numero = max(notas)
menor_numero = min(notas)

for nota in notas:
    print(nota)

print(f"É o maior: {maior_numero}")
print(f"É o menor: {menor_numero}")
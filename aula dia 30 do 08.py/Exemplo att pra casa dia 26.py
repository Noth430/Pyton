import os 
os.system("cls || clear")
QUANTIDADE_NOTAS = 3
soma = 0

for i in range(3):
    nota = float(input(f"Digite {i+1} Nota: "))

    if nota < 0 or nota > 10:
        print("Nota Inválida! \nDigitte Novamente: ")
    else:
        # soma = soma + nota
        soma += nota
        break
    
media =  soma / QUANTIDADE_NOTAS 

if media >=7:
    print("Aprovado.")
elif media >=5:
    print("Recuperação")
else:
    print("Reprovado")


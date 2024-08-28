import os 
os.system("cls || clear")
"""
Escreva um algoritmo que solitice duas notas para um aluno,caso seja menor que 0 ou maior que 10,mostre a pergunta novamente,calcule e mostre a média aritimetica do aluno.
"""

while True:
    primeira_nota = float(input("Digite uma nota"))
    segunda_nota = float(input("Digite a segunda nota"))

    if (primeira_nota  <0 or primeira_nota > 10) or (segunda_nota <0 or segunda_nota >10):
        print("\nA nota deve ser maior ou igual a 0 e menor e igual a 10")
       #elif segunda nota < 0 or segunda nota >10  
    else:
        break
soma = primeira_nota + segunda_nota
media = soma/2
    

print(f"Nota: {primeira_nota},{segunda_nota}")    
print(f"Media é {media}")

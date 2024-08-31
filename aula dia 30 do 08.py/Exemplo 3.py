"""
Escreva um algoritmo que pergunte ao usuário se deseja inserir mais uma nota.
Mostre um menu conforme o descrito abaixo:

S – Inserir mais uma nota;
P – Ver quantas notas foram inseridas;
N – Calcular a média aritmética das notas informadas.

O programa deve mostrar a média aritmética para o usuário.

"""

import os
import time

os.system("clear")

soma : float = 0
quantidadeNotas = 0

while True :

    print("""
        \t=== MENU ===
        S - Inserir uma nota
        P - Ver quantas notas foram inseridas
        N - Calcular média aritmética
    """)
   
    resposta = input("Deseja inserir uma nota: ").upper()
   
    match  resposta:
        case "S":
            nota = float(input("\nDigite uma nota: "))
            soma += nota
            quantidadeNotas += 1

        case "P":
            if quantidadeNotas == 0:
                print("Não foram inseridas notas. \n")            
                input("Pressione uma tecla para continuar...")
                time.sleep(3)
            else:
                print(f"Quantidade de notas inseridas: {quantidadeNotas} \n")
                input("Pressione uma tecla para continuar...")
               
        case "N":
            if quantidadeNotas == 0:
                print("Não foram inseridas notas. \n")
            else:
                break

        case _:
            print("Opção inválida... \n")
            time.sleep(3)

media  = soma / quantidadeNotas

print(f"Média: {media}")
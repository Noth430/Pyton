import os 
import time
os.system("cls || clear")
quantidadeNotas = 0
soma = 0

for i in range(3):
    nota = float(input(f"Digite {i+1} Nota: "))

    if nota < 0 or nota > 10:
        print("Nota Inválida! \nDigitte Novamente: ")
    else:
        # soma = soma + nota
        soma += nota
        break      
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


            media =  soma / quantidadeNotas

            if media >=7:
                print("Aprovado.")
            elif media >=5: 
                print("Recuperação")
            else:
                print("Reprovado")
                break

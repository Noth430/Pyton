""""
A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, coletando dados sobre o salário e número de filhos das famílias da cidade. Aprefeitura deseja saber

a) total de famílias que responderam a pesquisa;
b)média do salário da população;
c) média do números de filhos;
d) maior salário;
e) menor salário.

Crie um menu com as seguintes opções.
código | descrição
  1       Adicionar família
  2       Exibir rsultados
  3       Sair

Ao adicionar uma família, deve-se limpar o terminal e apresentar o menu novamente.
1. Salve os dados em um arquivo com nome: pesquisa_prefeitura.txt
2. O programa deve ler o arquivo para exibir os dados salvos.
"""
"""
Membros da Equipe:
1- Henrique Santos
2- Gabriel Pinto dos Santos

"""
import os 
os.system("cls || clear ")
from dataclasses import dataclass

quantidade_de_familiares = 1
lista_familiares = []
lista_salario = []
contator = 0
media = 0
soma_salario = 0
soma_fihos = 0



while True:
    
        print("""
             === MENU ===
            1 - Adicionar família
            2 - Exibir resultados
            3 - Sair
        
        """)

        resposta = int(input("deseja adicionar mais uma familia? "))

        match resposta:
            case 1:
                    quantidade_filhos = int(input("digite a sua quantidade de filhos: "))
                    salario = float(input("digite seu salario: "))
                    
                    contator += 1
                    lista_familiares.append(quantidade_filhos)
                    lista_salario.append(salario)
                
            case 2:
                print(f"familias que responderam: {contator}")
                maiorsalario =max(lista_salario)
                menorsalario =min(lista_salario)
                soma_salario =sum(lista_salario)
                media_salario = soma_salario / contator
                soma_flihos =sum(lista_familiares)
                media_filhos = soma_flihos / contator
                print(f"maior salario: {maiorsalario}")
                print(f"menor salario: {menorsalario}")
                print(f"quantidade de filhos: {quantidade_filhos}")
                print(f"media  salarial:  {media_salario}")
                print(f"media de filhos:  {media_filhos}")
                
                
                break
            case 3:
                print("===programa finalizado===")
                break    
            case _:
                print("opção invalida")

nome_arquivo = "arquivo_familia.txt"

with open(nome_arquivo, "a") as arquivo_familia:
    for i in range(1):
        arquivo_familia.write(f"familias que responderam{contator} ,media  salarial:  {media_salario},media de filhos:  {media_filhos}, maior salario: {maiorsalario}, menor salario: {menorsalario}\n  ")
arquivo_familia.close()
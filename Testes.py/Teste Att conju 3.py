import os
from dataclasses import dataclass

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

@dataclass
class Familia:
    quantida_filho: int
    salario: float

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def adicionar_familia(dados):
    quantida_filho = int(input("Digite a quantidade de filhos em sua família: "))        
    salario = float(input("Digite o salário da família: "))
    familia = Familia(quantida_filho, salario)
    dados.append(familia)

    # Salvar no arquivo
    with open('pesquisa_prefeitura.txt', 'a') as f:
        f.write(f"{familia.quantida_filho},{familia.salario}\n")

def exibir_resultados(dados):
    if not dados:
        print("Nenhuma família foi adicionada.")
        return

    total_familias = len(dados)
    salarios = [familia.salario for familia in dados]
    filhos = [familia.quantida_filho for familia in dados]

    media_salario = sum(salarios) / total_familias
    media_filhos = sum(filhos) / total_familias
    maior_salario = max(salarios)
    menor_salario = min(salarios)

    print(f"Total de famílias: {total_familias}")
    print(f"Média do salário da população: {media_salario:.2f}")
    print(f"Média do número de filhos: {media_filhos:.2f}")
    print(f"Maior salário: {maior_salario:.2f}")
    print(f"Menor salário: {menor_salario:.2f}")

def carregar_dados():
    dados = []
    
    # Tenta abrir o arquivo e carregar os dados
    arquivo = open('pesquisa_prefeitura.txt', 'r')  # Pode gerar erro se o arquivo não existir
    for linha in arquivo:
        quantida_filho, salario = linha.strip().split(',')
        dados.append(Familia(int(quantida_filho), float(salario)))
    arquivo.close()  # Certifica-se de fechar o arquivo
    
    return dados

def main():
    # Cria o arquivo se não existir
    if not os.path.isfile('pesquisa_prefeitura.txt'):
        open('pesquisa_prefeitura.txt', 'w').close()

    dados = carregar_dados()
    
    while True:
        clear_terminal()
        print("Menu:")
        print("1 - Adicionar família")
        print("2 - Exibir resultados")
        print("3 - Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            adicionar_familia(dados)
        elif escolha == '2':
            exibir_resultados(dados)
            input("Pressione Enter para continuar...")
        elif escolha == '3':
            break
        else:
            print("Opção inválida. Tente novamente.")

# Chamando a função main diretamente
main()
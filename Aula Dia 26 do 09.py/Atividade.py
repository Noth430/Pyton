import os
os.system("cls || clear")
from dataclasses import dataclass
# CRUD

#[x] CREATE
#[X] READ
# UPDATE
# DELETE

#Estrutura de dados.

@dataclass
class Cliente:
    nome: str
    sobrenome: str
    idade: int
    peso: float
    altura: float

QUANTIDADE_INFORMACOES = 4

lista_de_informacoes = []
for i in range(QUANTIDADE_INFORMACOES):
    cliente = Cliente(
    
        nome = input("Digite seu nome: "),
        sobrenome = input("Digite seu sobrenome"),
        idade = int(input("Digite sua idade: ")),
        peso = float(input("Digite seu peso: ")),
        altura = float(input("Digite sua altura: "))
    )
    lista_de_informacoes.append(cliente)

nome_do_arquivo = "carteira_de_clientes.txt"

with open(nome_do_arquivo, "w") as arquivos_clientes:
    for cliente in lista_de_informacoes:
        arquivos_clientes.write(f"{cliente.nome},{cliente.sobrenome},{cliente.idade},{cliente.peso},{cliente.altura}\n")

for cliente in lista_de_informacoes:
    print(f"Nome: {cliente.nome}")
    print(f"Sobrenome: {cliente.sobrenome}")
    print(f"Idade: {cliente.idade}")
    print(f"Peso: {cliente.peso}")
    print(f"Altura: {cliente.altura}")

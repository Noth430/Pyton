import os 
os.system("cls || clear")

lista_vetores = []


for i in range(2):
    numero = int(input("Digite um numero"))
    lista_vetores.append(numero)



def opcao(numeros):
    
    multiplicacao = 1
    for numero in numeros:
        multiplicacao *= numero
        
    return multiplicacao


verificacao = opcao(lista_vetores)

for numero in lista_vetores:
    print(numero)



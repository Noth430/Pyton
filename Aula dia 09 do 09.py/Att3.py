import os 
os.system("cls || clear")

contador = 0
soma = 0
for i in range(3):
        nota = float(input("Digite uma nota: "))
        contador += 1
        soma += nota
def media(n1,contador):
    
    
    media = n1/contador

    return media
    
resultado = media(soma,contador)
print(f"Media: {resultado}")




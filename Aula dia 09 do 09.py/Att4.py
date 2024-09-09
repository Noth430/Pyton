import os
os.system("cls || clear")

altura = float(input("Digite sua altura: "))

peso = float(input("Digite seu peso: "))

def imc(n1,n2):
    
    resposta = n2 / (n1 * n1)

    return resposta

resposta = imc(altura,peso)

if resposta >= 40:
        print("Obesidade grau 3: ")
elif resposta >= 35:
        print("Obesidade grau 2: ")
elif resposta >= 30:
        print("Obesidade grau 1: ")
elif resposta >= 25:
       print("Sobrepeso: ")
elif resposta >=18.5:
       print("Peso normal: ")
elif resposta <= 18.5:
       print("Abaixo do peso: ")


print(f"Imc: {resposta:.2f}")

import os 
os.system("cls || clear")
contador = 0
soma = 0
orcamento=float(input("Informe um teto de gasto"))
while True:
    for i in range(1):
        gasto = float(input("digite um valor: "))
        soma += gasto
        contador += 0

    if gasto > orcamento:
        print(f"Valor mensal: {gasto}")
        break
      
        





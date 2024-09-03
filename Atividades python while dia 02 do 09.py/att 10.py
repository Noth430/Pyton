import os 
os.system("cls || clear")

total_calorias = 0

while total_calorias <= 2000:
    calorias_refeicao = float(input("Digite o número de calorias consumidas nesta refeição: "))
    total_calorias += calorias_refeicao

    excesso_calorias = total_calorias - 2000
    print(f"Você consumiu um total de {total_calorias:.2f} calorias.")
    print(f"Você excedeu sua meta em {excesso_calorias:.2f} calorias.")

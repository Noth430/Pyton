import os 
os.system("cls || clear")


meta = float(input("Digite sua meta de horas de estudo: "))
total_horas = 0

while total_horas < meta:
    horas_estudadas = float(input("Digite o número de horas estudadas hoje: "))
    total_horas += horas_estudadas
    excedente = total_horas - meta
    if excedente > 0:
        print(f"Parabéns! Você atingiu sua meta e ainda estudou {excedente:.2f} horas a mais.")
    else:
        print(f"Você atingiu sua meta de {meta} horas de estudo!")

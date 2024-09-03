import os 
os.system("cls || clear")
orcamento=float(input("\nInforme um orçamento"))
gasto_total = 0

while True:
        gasto_diario = float(input("\ndigite um valor: "))
        if gasto_diario == 0:
              break
        gasto_total += gasto_diario
        
        if gasto_total > orcamento:
          exedente = gasto_total - orcamento
          print(f"Você gastou R${gasto_total:.2f}. Excedeu seu orçamento em R${exedente}: ")
        else:
             print(f"Você gastou R${gasto_total:.2f}. Valor total dentro do orçamento ")
      
        



import os 
os.system("cls || clear")
peso_ideal = 0


altura = float(input("informe sua altura"))

sexo = input("informe seu sexo(M ou F):").upper()

match(sexo):
    
 case "M":   
       peso_ideal = (72.7* altura) - 58
 case "f":
    peso_ideal = (62.1 * altura) - 44.7
 case _:
      print("opção invalida")

print(f"sexo: {sexo}")
print(f"peso idal: {peso_ideal:.2f}")
    
                  

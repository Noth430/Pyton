import os 
os.system("cls || clear")

tentativas = 3
contador = 0    
desconto = 0
while True:
    
    desconto = input("digite o codigo de desconto para receber o desconto : ")
    
    if desconto == "PROMO2024":
        print("Desconto Aplicado")   
    else:
        print("tente novamente")
    contador += 1
    if contador == tentativas:
        break    
    

        
    
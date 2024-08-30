import os 
os.system("cls || clear")


soma = 0
contador = 0
media = 0
while True:
    nota = float(input("digite uma nota: "))
    contador += 1
    soma += nota
    
    opcoes = int(input("escolha uma opção: "))
    resposta = input("Deseja inserir mais uma nota? ")
    #resposta = resposta.upper()#converter em maiusculo.

    match resposta:
         case 1:
            
         

         
         break
    
    

media = soma / contador
print(f"Media: {media}")

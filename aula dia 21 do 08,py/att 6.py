import os 
os.system("cls || clear")
 
print("""
     1-picanha
    
     2-lasanha
    
     3-strogonof
    
     4-ife acebolado
    
     5 pão com ovos
      """)         



cardapio = int(input("escolha uma opão do menu"))
match(cardapio):

    case 1:
        print("Prato:picanha")
        print("Preço: R$ 25,00")
    case 2:
        print("Prato:lasanha")
        print("Preço: 20,00 ")
    case 3:
        print("Prato:strogonof")
        print("Preço: R$15,00")
    case 4:
        print("Prato:bife acebolado")
        print("valor R$10,00")
    case 5:
        print("Prato:pão com ovos")
        print("valor R$ 5,00")

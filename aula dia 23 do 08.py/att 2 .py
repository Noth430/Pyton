import os 
os.system("cls || clear")

desconto = 0
preco_final = 0
preco_parcelado = 0

print("solicitando dados para o usuário")
preco_produto = int(input("digitre o valor do prutdo"))

print("\nEscolha uma das formas de pagamento abaixo ")
print("1 - pagamento a vista")
print("2 - pagamento a prazo")
opcao = int(input("Informe a opção desejada"))

match(opcao):
    
    case 1:
        desconto = preco_produto *0.10
        preco_final = preco_produto - desconto

        print(f"\npreco do produto: R$ {preco_produto}")
        print(f"forma de pagamento a vista")
        print(f"valor do desconto: R$ {desconto}")
        print(f"total a pagar: R$ {preco_final}")

    case 2:
        parcelas = int(input("\ndigite a quantidade de parcelas: "))    

        preco_parcelado = preco_produto / parcelas
        preco_final = preco_produto

        print(f"\npreço do produto: R$ {preco_produto}")
        print(f"forma de pagamento: a prazo")
        print(f"quantidade de parcelas: {parcelas}")
        print(f"valor por parcelas R$ {preco_parcelado:.2f}")
    
    case _:
        print("opção invalida")
                                


  


    

   



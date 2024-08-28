import os 
os.system("cls || clear")

print("""

1 - cadastrar usuário 
2 - excluir usuário
3 - sair do sistema
    """)
opcao = int(input("digite uma opção"))

match(opcao):

 case 1:
    print("opção cadastras usuário.")
 case 2:
    print("opção exluir usuário.")
 case 3:
    print("opção de sair ")

print("==fim==")
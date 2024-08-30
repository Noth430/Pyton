import os 
os.system("cls || clear")


for i in range(1):
       while True:
            nota = float(input("Digite uma nota"))
        
       
        soma = primeira_nota + segunda_nota + terceira_nota
        media = soma/3
    

        if (primeira_nota  <0 or primeira_nota > 10) or (segunda_nota <0 or segunda_nota >10):
                float(input("\nA nota deve ser maior ou igual a 0 e menor e igual a 10"))
        elif terceira_nota <0 or terceira_nota >10:
                float(input("\nA nota deve ser maior ou igual a 0 e menor e igual a 10")) 
        elif media >= 7: 
                print("Aluno Aprovado")
        elif media >= 5 and  media <= 6.9:
                print("Aluno em recuperação")
        else:
                print("Aluno Reprovado")
    
    
    
        


import os 
os.system("cls || clear")
            
for i in range(1):
        n1 = float(input('Digite a primeira nota: '))
        n2 = float(input('Digite a segunda nota: '))
        n3 = float(input('Digite a terceira nota: '))

        soma = n1 + n2 +n3

        media = soma / 3

        media_aprovada = 7

while n1 < 0 or n1 > 10 or n2 < 0 or n2 > 10 or n3 < 0 or n3 > 10:
    n1 = float(input('Nota inválida! Digite a primeira nota: '))
    n2 = float(input('Nota inválida! Digite a segunda nota: '))
    n3 = float(input('Nota inválida! Digite a terceira nota: '))
        
if media < 5:
        print(f'Reprovado! Sua média foi {media}')

elif 5 <= media <= 6.9:
        print(f'recuperação! Sua média foi {media}')

else:
        print(f'Aprovado! Sua média foi {media}')
    
        
        print("deseja digita uma nova nota ? ")

          
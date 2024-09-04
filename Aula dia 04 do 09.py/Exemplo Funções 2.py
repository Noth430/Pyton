import os 
os.system("cls || clear")

#Função com retorno.
def somar(n1,n2):
    soma = n1 + n2
    return soma


primeiro_numero = int(input("digite um numero"))
segundo_numero = int(input("digite um numero"))

soma = somar(primeiro_numero, segundo_numero)

print(f"Soma: {soma}")

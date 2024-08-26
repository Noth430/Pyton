import os 
os.system("cls || clear")

#for i in range(1,11):
    #print(f"{2} * {i} = {2 * i} ")

#solicitando dados.

numero = int(input("digite um nomero:"))
print(f"\n tabuada de multiplicação do numero: {numero}")
for i in range(1,11):
    print(f"{numero} * {i} = {numero * i} ")
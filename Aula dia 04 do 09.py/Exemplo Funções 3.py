import os 
os.system("cls || clear")

def desconto_salario(salario_bruto):
    vale_transport = 200
    vale_refeicao = 200
    plano_de_saude =300

    resultado = salario_bruto - vale_transport-vale_refeicao-plano_de_saude
    return resultado

salario_bruto = float(input("Digite o valor do seu salário bruto: "))

salario_liquido = desconto_salario(salario_bruto)

print(f"Salario líquido: {salario_liquido}")
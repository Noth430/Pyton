import os 
os.system("cls || clear")

def somar(n1,n2):
    
    soma = n1 + n2 

    return soma

def subtracao(n3,n4):
    
    subtracao = n3 - n4

    
    return subtracao

def divisao(n7,n8): 
    soma = n7 + n8    
    divisao = soma/2

    return divisao

def multiplicacao(n5,n6):
    
    multiplicacao = n5 * n6

    return multiplicacao


numero = int(input("Digite um numero: "))

numero2 = int(input("Digite um numero: "))

soma = somar(numero,numero2)

print(f"Soma: {soma} ")

subtracao1 = subtracao(numero,numero2)

print(f"Subtração: {subtracao1} ")

dividir = divisao(numero,numero2)

print(f"Divisão: {dividir}")

multiplicar = multiplicacao(numero,numero2)

print(f"Multiplicação: {multiplicar}" )

# Ex 1
#entrada
num1 = int(input("Digite o primeiro numero"))
num2 = int(input("Digite o segundo numero"))
#processamento
soma = num1 + num2
#saída
print(soma)

#Ex 
#Entrada
num1 = int(input("Digite o primeiro numero"))
#processamento
if num1 % 2 == 0:
    print("Par")
else:
    print("Ímpar")

#3.	Escrever um programa que leia três números inteiros e determine a média deles.
#Entrada
num1 = int(input("Digite um numeo inteiro"))
num2 = int(input("Digite um numeo inteiro"))
num3 = int(input("Digite um numeo inteiro"))
#processamento 
maior_numero = max(num1, num2, num3)
num = (num1 + num2 + num3) /3
#saída
print(num)

#4 Escrever um programa que leia três números inteiros e determine qual deles é o maior.
num1 = int(input("Digite um numeo inteiro"))
num2 = int(input("Digite um numeo inteiro"))
num3 = int(input("Digite um numeo inteiro"))
#processamento
num = max(num1, num2, num3)

#5 Criar uma calculadora simples que permita ao usuário realizar operações básicas (soma, subtração, multiplicação, divisão).
num1 = int(input("Digite um numeo inteiro"))
num2 = int(input("Digite um numeo inteiro"))
operacao = (input("Digite uma operação"))

def calculadora(num1, num2, operacao):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
    elif operacao == '*':
        return num1 * num2
    elif operacao == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Erro: Divisão por zero"
    else:
        return "Operação inválida"

# Exemplo de uso
#num1 = 8
#num2 = 4
#operacao = '/'

resultado = calculadora(num1, num2, operacao)
print(resultado)
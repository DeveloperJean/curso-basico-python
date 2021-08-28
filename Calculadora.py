# -*- coding: utf-8 -*-
"""
Calculadora
Autor: Jean Andrade
Função: fazer contas: soma, divisão, multiplicação, subtração
"""

print("---- CALCULADORA v2.0 ----")

sair = False
while sair == False:

	num1 = input("Digite o primeiro número: ")
	num1 = int(num1)
	operador = input("Digite o operador (+-/*): ")
	num2 = input("Digite o segundo número: ")
	num2 = int(num2)

	# + soma

	if operador == "+":
		operacao = num1 + num2

	# - subtracao
	if operador == "-":
		operacao = num1 - num2

	# / divisao	
	if operador == "/":
		operacao = num1 / num2

	# * multiplicação
	if operador == "*":
		operacao = num1 * num2

	print("Resultado: ")
	print(operacao)

	teste = input("Deseja sair (n\s): ")
	if teste == "s":
		sair = True
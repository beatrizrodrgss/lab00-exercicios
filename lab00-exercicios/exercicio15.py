# Escreva um programa que leia, como entrada, o valor de um número inteiro positivo.
# Como saída, imprima o dobro do valor digitado.

numero = int(input("Digite o numero: "))

if numero > 0:
	dobro = numero * 2

	print(dobro)

else:
	print("Digite um número")
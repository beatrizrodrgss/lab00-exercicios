# Seis amigos foram a um restaurante. A conta deu R$ 250, a ser repartida igualmente para cada um.
# Escreva um programa que imprima o valor que cada um tem que desembolsar.
# O resultado deve ser apresentado com, no máximo, duas casas decimais, indicativas dos centavos.

valor_total_conta = 250
numero_amigos = 6

valor_por_amigo = valor_total_conta / numero_amigos
valor_por_amigo_arredondado = round(valor_por_amigo, 2)

print(valor_por_amigo_arredondado)
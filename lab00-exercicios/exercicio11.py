# A área A de um hexágono regular, de aresta a, é dada por:
# A = 3 sobre 2 raiz quaadrada de 3 a ao quadrado
# Escreva um programa que calcule e imprima o valor da área de um hexágono de 5 cm de aresta, aplicando a fórmula acima.
# Exiba o resultado com até quatro casas decimais de precisão.

aresta = 5
raiz = 3**0.5
area = 3 / 2 * raiz * aresta**2
 
print(round(area, 4))
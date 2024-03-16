# Um grupo de três guerreiros derrotou um monstro que escondia 50 moedas de ouro. 
# Cada um vai receber a mesma quantia de moedas e o restante será pago a um informante que indicou o caminho até o covil do monstro.
# Escreva um programa que determine:
# Quantas moedas de ouro cada guerreiro receberá?
# Quantas moedas de ouro serão pagas ao informante?

# Quantidade de moedas de ouro e número de guerreiros
moedas_ouro_total = 50
numero_guerreiros = 3

moedas_por_guerreiro = moedas_ouro_total // numero_guerreiros

moedas_para_informante = moedas_ouro_total - (moedas_por_guerreiro * numero_guerreiros)

print(moedas_por_guerreiro)
print(moedas_para_informante)

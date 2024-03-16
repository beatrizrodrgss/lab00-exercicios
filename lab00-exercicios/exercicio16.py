# Elabore um programa que leia o ano corrente. Consulte o ano de fundação do IFAM (consulte o Google, se você não souber).
# Qual o resultado do comando abaixo? Troque o YYYY pela variável que você leu na entrada e XXXX pelo ano de fundação do IFAM.
# print("Em ",YYYY,"o IFAM completou", YYYY - XXXX, "anos de fundacao.")

ano_corrente = int(input("Digite o ano corrente: "))

ano_fundacao = 2008

anos_fundacao = ano_corrente - ano_fundacao

print("Em ", ano_corrente,"o IFAM completou", anos_fundacao, "anos de fundacao.")
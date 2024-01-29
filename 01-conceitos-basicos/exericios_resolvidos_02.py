#Elabore um programa em que você lançará a cotação do dólar do dia e um determinado valor em real e será impresso, ao final, quantos dólares correspondem àquele valor.

cotacao_dolar_hoje = 4.95

valor_reais = 1000.0

valor_convertido = valor_reais / cotacao_dolar_hoje

print('R$ %.2f correspondem a US$ %.2f hoje' %(valor_reais, valor_convertido))
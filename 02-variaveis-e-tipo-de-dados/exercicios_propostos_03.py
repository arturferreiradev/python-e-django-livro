# No Exercício resolvido 2 do Capítulo 1, mostrei como criar um programa bastante simplificado que converte valores de dólares para reais. Com seus novos conhecimentos sobre como ler dados a partir da entrada padrão (teclado), crie uma nova versão daquele código, que pedirá a cotação do dólar do dia, uma quantidade de reais e exibirá o valor convertido para dólares. Aproveite para formatar os dados com os símbolos de R$ e US$ e colocar duas casas decimais no resultado.

cotacao_dolar_hoje = float(input('Digite a cotação do dólar hoje: '))

valor_reais = float(input('Digite o valor em reais a ser convertido: '))

valor_convertido = valor_reais / cotacao_dolar_hoje

print('R$ %.2f correspondem a US$ %.2f hoje' %(valor_reais, valor_convertido))
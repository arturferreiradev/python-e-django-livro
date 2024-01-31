# Escreva um programa que solicita as dimensões (largura e comprimento) de uma sala em metros, o tamanho da aresta de uma peça quadrada de cerâmica em cm e o preço do metro quadrado da referida cerâmica; imprima quantos metros quadrados devem ser adquiridos para pavimentar a referida sala e descubra quanto custará a cerâmica a ser usada.

print("Cálculo de custo cerâmica")

comprimento = float(input("Qual o comprimento da sala em metros: "))
largura = float(input("Qual a largura da sala em metros: "))
aresta_da_ceramica = float(input("Qual o tamanho da aresta em cm: "))
preco_metro_ceramica = float(input("Qual o valor do metro da cerâmica: "))
sala_em_m2 = comprimento * largura
valor_a_pagar = sala_em_m2 * preco_metro_ceramica
print('O valor a pagar é de %.2f' % valor_a_pagar)



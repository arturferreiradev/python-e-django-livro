# Crie um programa em que serão fornecidas a altura, largura e profundidade de uma caixa d’água em forma de paralelepípedo retângulo em metros, e será impressa na tela a capacidade em litros do referido recipiente (dica: volume = altura x largura x profundidade e 1m3 = 1.000 litros).

altura = 2
largura = 3
profundidade = 5

qtde_litros = altura * largura * profundidade * 1000

print('Uma caixa com as dimensões %dx%dx%d em metros tem a capacidade de %d litros' %(altura, largura, profundidade, qtde_litros))
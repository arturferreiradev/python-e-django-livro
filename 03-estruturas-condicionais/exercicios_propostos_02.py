# Crie um programa que solicitará ao usuário as medidas de três lados de um triângulo e informará como saída se os valores formam um triângulo retângulo. Os lados devem ser fornecidos em qualquer ordem (ou seja, não “vale” escrever “digite o tamanho da hipotenusa”, “digite o tamanho do cateto 1” etc.). Dica: use o Teorema de Pitágoras (“O quadrado da hipotenusa é igual à soma dos quadrados dos catetos”).

lado_1 = float(input('Digite o tamanho de um dos lados do triângulo: '))
lado_2 = float(input('Digite o tamanho de um dos lados do triângulo: '))
lado_3 = float(input('Digite o tamanho de um dos lados do triângulo: '))

if((lado_1 ** 2 + lado_2 ** 2)  == lado_3 ** 2):
    print("Os lados informados formam um triângulo retângulo")
elif((lado_2 ** 2 + lado_3 ** 2) ** 2 == lado_1 ** 2):
    print("Os lados informados formam um triângulo retângulo")
elif((lado_3 ** 2 + lado_1** 2 ) ** 2 == lado_2 ** 2):
    print("Os lados informados formam um triângulo retângulo")
else:
    print("Os lados informados não formam um triângulo retângulo")
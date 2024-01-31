# Em estatística, uma mediana é um valor que divide uma amostra ao meio, com os elementos menores que a mediana à esquerda desta; e os maiores, à direita. Faça um programa que solicita três números inteiros ao usuário e imprime a média aritmética simples e a mediana dos três. A mediana, em muitos casos, é uma medida de tendência central mais adequada que a média, pois é menos influenciada por valores extremos.

valores = [0, 0, 0]
numero = int(input("Digite um numero inteiro: "))
if(numero > valores[2]):
    valores[2] = numero
numero = int(input("Digite um numero inteiro: "))
if(numero > valores[2]):
    valores[1] = valores [2]
    valores[2] = numero
else:
    valores[1] = numero
numero = int(input("Digite um numero inteiro: "))
if(numero > valores [2]):
    valores[0] = valores[1]
    valores[1] = valores[2]
    valores[2] = numero
elif(numero > valores[1]):
    valores[0] = valores[1]
    valores[1] = numero
else:
    valores[0] = numero

media_valores = float(valores[0] + valores[1] + valores[2] / 3)
mediana = valores[1]

print("O valor da média é %.2f, o valor da mediana é %d" %(media_valores, mediana))



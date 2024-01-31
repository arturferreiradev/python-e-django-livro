# Crie um programa que receba cinco números inteiros e os imprima na ordem inversa em que foram digitados. Dica: armazene os números em uma lista.

print("Inversão de números")
valores = [0, 0, 0, 0, 0]
numero = int(input("Digite o primeiro número: "))
valores[4] = numero
numero = int(input("Digite o segundo número: "))
valores[3] = numero
numero = int(input("Digite o terceiro número: "))
valores[2] = numero
numero = int(input("Digite o quarto número: "))
valores[1] = numero
numero = int(input("Digite o quinto número: "))
valores[0] = numero
print("Os valores digitados em ordem inversa foram %d, %d, %d, %d, %d" % (valores[0], valores[1], valores[2], valores[3], valores[4]))

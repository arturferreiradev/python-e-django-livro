# Faça um programa que solicite dois números inteiros ao usuário e imprima o maior deles.

numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))

if numero1 > numero2:
    print(f'O maior deles é {numero1}')
elif numero1 < numero2:
    print(f'O maior deles é {numero2}')
else:
    print('Os números são iguais!')
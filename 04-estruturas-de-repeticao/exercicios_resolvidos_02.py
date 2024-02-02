# Escreva um programa que lista todos os números entre 1.000 e 5.000 (incluindo os dois extremos) que são divisíveis por 5 e 3 ao mesmo tempo. Ao final, imprima a quantidade de números que satisfazem essas condições.

contador = 0

for x in range(1000,5001):
    if(x % 3 == 0) and (x % 5 == 0):
        print(f'{x} é dívisivel, simultaneamente por 3 e 5')
        contador = contador + 1

print(f'Há {contador} números divisiveis por 3 e 5 entre 1000 e 5000')